
"""Yelkovan

Yelkovan is a program analyser for RISC-V architecture. It detects 
basic blocks of risc-v assembly code and creates the control flow graph of the 
program. The cfg is outputted to command line as text and to pdf file as figure. 

The detection of the basic blocks is performed by the help of trace information 
of the program. Yelkovan analyses the trace files created by gem5 architecture 
simulator.

Yelkovan takes two types of input files. Assembly file of the program and
trace files of the program. To be able to create a cfg of the a program perform
the following steps:

1. Create the assembly file of the program's executable file by the help of 
objdump tool which is delivered with the RISC-V compiler toolchain.
2. Give ".dump" extension to the assembly file.
3. Create trace files of the program by using gem5 architecture simulator.
4. Give ".trc" extension to the trace files.
5. Put above mentioned files to the working directory of Yelkovan.
6. Run Yelkovan.
7. The text outuput is going to be shown in command line interface, and the
graphical output is created as a pdf file in the working directory.

Yelkovan Defaults
- Line numbers in Yelkovan starts with 0.
- Addresses of instructions are in hexadecimal format and does not include
additional symbols like "0x", "h", etc. A sample address is "100c8".

"""

# Assembly tools of Yelkovan which includes functions that help processing 
# assembly file.
import asm_tools

# Trace tools of Yelkovan which includes functions that help processing 
# trace files.
import trace_tools


# Type hints support regarding collections
from typing import List, Set, Dict, Tuple, Optional

# List sorting
from operator import itemgetter

# Directory listing
from os import linesep, listdir

# Graph operations
import networkx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph

# Graph visualization
import pygraphviz



# Line numbers of starting points of basic blocks.
# In this list each item represents the start of a basic block.
start_list: List[int] = []

# Line numbers of end points and line numbers of targets of basic blocks.
# In this list each item represents the end of a basic block. The first element
# of the item is the line number of the end of a basic block. The other elements 
# (if present) of the item represent the targets of the basic block.
end_list: List[List[int]] = []

# This is the stack like data structure which holds the starting line numbers
# of functions which will be visited and processed for basic block
# detection. During the analysis when we encounter a function we add it to this
# list. When we visit a function we pop that function from this list.
will_be_visited_fn_list = []

# Conditional branch instructions
branch_inst = ["beq", "bne", "blt", "bltu", "bge", "bgeu", "beqz", "bnez",
    "bltz", "blez", "bgtz", "bgez", "bgt", "bgtu", "ble", "bleu"]

# Unconditional jump instruction
jump_inst = ["ret", "jal", "j", "jalr", "jr"]


# The set of nodes which have already been added to the the control flow graph 
# of the program.
# Each item in the set is an integer which represents the starting point of a 
# basic block. By the help of this set, we know if a node is already in the 
# control flow graph or not. We use this set in the creation of the control
# flow graph to prevent duplicate entries.
cfg_set = set()


# Starting line number of the root node of the graph.
root_node = 0



def main() -> None:
    """Main function of Yelkovan.

    This function is called by the entry point of the Yelkovan. This function
    searches the current directory for assembly file and trace files of the
    program and then calls analyse function for program structure analysis.
    """

    # Assembly file
    assembly_file: str = None

    # List of trace files.
    trace_files: List[str] = []


    # listdir function returns a list of strings which represent file names.
    for file_name in listdir("./"):
        if file_name.endswith(".trc"):
            trace_files.append(file_name)
        elif file_name.endswith(".dump"):
            assembly_file = file_name

    # If there is no trace file, raise exception.
    if not trace_files:
        raise Exception("Trace files are not found. Please make sure at least a "
                        "trace file is present with \".trc\" extension in the "
                        "current working directory.")

    # If there is no assembly file, raise exception.
    if assembly_file == None:
        raise Exception("Assembly file is not found. Please make sure an assembly " 
                        "file is present with \".dump\" extension in the current "
                        "working directory.")


    analyse(assembly_file, trace_files)


def analyse(assembly_file: str, trace_files: list) -> None:
    """Analyses the contents of the assembly file.

    This function is the main function who starts and manages basic block
    detection operation.

    Parameters
    ----------
    assembly_file : str
        Name of the assembly file of the program.
    trace_files : list of str
        List of names of the trace files of the program.
    """


    visited_fn_list = []

    global start_list
    global end_list
    global will_be_visited_fn_list


    with open(assembly_file) as f:
        content = f.read()
    f.closed

    assembly_code = content.splitlines()


    # Find main function and add to it to the will be visited function list.
    # It is the first function in this list.
    line_no = asm_tools.get_function_start("main", assembly_code)
    will_be_visited_fn_list.append(line_no)

    while(will_be_visited_fn_list):

        line_no = will_be_visited_fn_list.pop()

        # If the starting line number of the function is not in visited function
        # list then add it to the list and process the related function.
        if (line_no not in visited_fn_list):
            visited_fn_list.append(line_no)
            process_fn(line_no, assembly_code, trace_files)

    # Sort start list.
    start_list = sorted(start_list)

    end_list.sort(key = itemgetter(0))
    #print(f"End list: {end_list}")
    # After making sure duplicate items are not in the end_list remove remove_duplicates function.
    #remove_duplicates()    
    #print(f"End list: {end_list}")
    check_targets(assembly_code)


    if (len(start_list) != len(end_list)):
        raise Exception("Error: Lengths of the start list and end list do not match!")

    # Create directed graph.
    cfg = networkx.DiGraph()
    root_node = asm_tools.get_function_start('main', assembly_code)
    create_di_graph(cfg, -1, root_node)

    # Configure the graph.
    cfg.graph['node']={'shape':'box', 'fontname':'sans', 'margin':'0.07', 'width':'0.1', 'height':'0.1'}
    # cfg.graph['edges']={'arrowsize':'1.0'}

    cfg_graph = to_agraph(cfg)
    print(cfg_graph)
    cfg_graph.layout('dot')
    cfg_graph.draw('cfg.pdf')


def add_item_to_end_list(end_point: int, target: List[int] = None) -> None:
    """Adds an item to the end list.
    
    Each item of this list may be a list depending on the end point.
    The first element of the item is the line number of the end point of a basic 
    block. The following elemnents of the item are the line numbers of targets
    of the end point of the basic block. When the end point of a basic block is 
    found this function is called to add it to start_list.

    This function first checks if the item is in the list or not.
    
    If the item is in the list its targets are checked not added. If the targets are also 
    in the list this function returns. If the target(s) are not present they are 
    added.

    If the item is not in the list, it is added with all of its targets.

    This function does not return a value.
    

    Parameters
    ----------
    end_point: int
        The line number of the end of a basic block which will be added to
        start_list.
    target: list of int
        The list of line numbers of the targets of the end point.
    """

    global end_list
    item_found: bool = False
    item_no: int = -1

    # Check if the end_point is alread in the end_list.
    for item in end_list:
        if item[0] == end_point:
            item_found = True
            break

    # If the list is empty or the end_point is not in the list add it.
    if item_found == False:
        end_list.append([end_point])

    # If there is no target information there is nothing more to do. Just return.
    if target is None:
        return

    # Find the index of the end_point.
    for index, item in enumerate(end_list):
        if item[0] == end_point:
            item_no = index
            break

    # Add targets to the end_point.
    for target_item in target:
        if target_item not in end_list[item_no]:
            end_list[item_no].append(target_item)                



def add_item_to_start_list(starting_point: int) -> None:
    """Adds an item to the start list.
    
    The item is the the line number of the starting point of the basic block. 
    When the starting point of a basic block is found this function is called to
    add it to start_list.

    This function first checks if the item is already in the list or not. If 
    the item is in the list it is not added. If it is not in the list it is 
    added.

    This function does not return a value.
    

    Parameters
    ----------
    starting_point : int
        The line number of the start of a basic block which will be added to
        start_list.
    """

    global start_list

    # If the item is not already in the start_list add it.
    if starting_point not in start_list:
        start_list.append(starting_point)


def create_di_graph(cfg: networkx.DiGraph, previous_node: int, 
                    current_node: int) -> None:
    """Creates control flow graph of the program.

    Note: This function is a recursive function.

    In control flow graph a node represents a basic block, and an edge
    represents the connection between two basic blocks. Starting line number of 
    a basic block is the id of the node which represents that basic block.

    Previous node and current node are id numbers of two nodes. In other words
    they are starting line numbers of two basic blocks. Current node is the new 
    node which will be added to the cfg. This function works as follows:

    1. It adds a new node to the cfg with the current_node id number. It updates
    the information of the node with the values from start_list and end_list.
    2. It adds an edge between the current node and previous node. Current node 
    is one of the targets of previous node.
    3. It checks the targets of the current node (newly added basic block) by
    looking at end_list. If there is a target information it calls itself again. 
    In the new call, the id number of newly added node (current_node) will be 
    passed as previous_node argument, and the target of the newly added node 
    will be passed as current_node argument.
    

    Parameters
    ----------
    cfg : directed graph
        This is the control flow graph of the program.
    previous_node : int
        The id number of the previous node. In other words the starting line
        number of the previous basic block.
    current_node : int
        The id number of the current node. In other words the starting line
        number of the current basic block. This node will be added to the
        control flow graph.
    """

    index = 0

    if (current_node in cfg_set) & (previous_node != -1):
        cfg.add_edge(previous_node, current_node)
        return

    for i in range(0, len(start_list)):
        if (start_list[i] == current_node):
            index = i

    cfg.add_node(current_node)
    cfg_set.add(current_node)

    if (previous_node != -1):
        cfg.add_edge(previous_node, current_node)

    cfg.nodes[current_node]['label'] = "Start: " + str(start_list[index]) + "; End: " + str(end_list[index][0])
    cfg.nodes[current_node]['start'] = start_list[index]
    cfg.nodes[current_node]['end'] = end_list[index][0]
    cfg.nodes[current_node]['target1'] = "null"
    cfg.nodes[current_node]['target2'] = "null"

    if (len(end_list[index]) == 2):
        # There is one target            
        cfg.nodes[current_node]['target1'] = end_list[index][1]
        create_di_graph(cfg, current_node, end_list[index][1])
    elif (len(end_list[index]) == 3):
        # There are two targets
        cfg.nodes[current_node]['target1'] = end_list[index][1]
        create_di_graph(cfg, current_node, end_list[index][1])
        cfg.nodes[current_node]['target2'] = end_list[index][2]
        create_di_graph(cfg, current_node, end_list[index][2])



def remove_duplicates() -> None:
    """Detects and removes the duplicate elements in the end_list.

    This function is called after analyzing the assembly code. During detection 
    we don't check duplicate end points. Therefore, after analyzing the file 
    there may be duplicate elements in the end_list. This function checks and 
    removes them.

    This function does not return a value. Instead it makes required 
    modifications to end_list.
    """

    result = -1    
    while(True):
        if (result != -1):
            del(end_list[result])
            result = -1

        found = False
        for index_1, item_1 in enumerate(end_list):    
            for index_2, item_2 in enumerate(end_list):
                if ((item_1[0] == item_2[0]) & (index_1 != index_2)):
                    found = True
                    if (len(item_1) >= len(item_2)):
                        result = index_2
                    else:
                        result = index_1
                    break

            if (found):
                break

        if (result == -1):
            break


def check_targets(assembly_code: list) -> None:
    """Checks the targets of basic blocks.
    
    This function is called afeter analyzing the assembly code. It is used to 
    check the targets of basic blocks. It detects targets of basic blocks which 
    are not detected until now. This only happens if a basic block's target is 
    the next line of the same basic block.

    Iterate all of the items in the end_list. The items of the end_list 
    represent end points of basic blocks. First element of an item is the line 
    number of the end point of a basic block. Other elements of an item are the
    targets of the basic block.
    
    If an item has not target information (basic block has not any 
    target) and is not the end of the main function, the next line of the item 
    should be the target of the item (the target of the basic block should be
    the next line).

    1. If the length of an item is 1 the item has not target information.
    2. If the line number of an item (item[0]) is different from the line number 
    of the end of main function, the item is not the end of the main function.
    In this case the next line of the item is the target of the item (basic 
    block).

    This function does not return a value. Instead it makes required
    modifications to end_list.

    Parameters
    ----------
    assembly_code : list of str
        Assembly code of the program. This is needed to find the line number of
        the last instruction of the main function.
    """

    # Find the line number of the last instruction of main function.
    main_function_end = asm_tools.get_function_end('main', assembly_code)

    for index, item in enumerate(end_list):
        if (len(item) == 1):
            if (item[0] != main_function_end):
                item = [item[0], item[0] + 1]
                end_list[index] = item



def process_fn(line_no: int, assembly_code: list, trace_files: list) -> None:
    """Detects basic blocks in a given funtion.

    Traverses a function in assembly code line by line and detects basic blocks.
    
    First it checks if the is null or not. If the line is null this means the
    end of the function is reached. In this case returns. If the line is not 
    null the line is tokenized and analyzed.

    If the length of the tokens is less than 3 the line is not a valid
    instruction. In this case processing continues with the next line.

    If the line is a "ret" (return from subroutine) instruction starting and
    end points of basic blocks are detected and written in start_list and
    end_list respectively.

    If the line is a branch or jump instruction the related functions which
    process them is called.
    
    This function does not return a value. Instead it adds the line numbers of
    the detected starting and end points of basic blocks to the start_list and
    end_list.

    Parameters
    ----------
    line_no : int
        Starting line number of the function which is going to be processed.
    assembly_code : list of str
        Assembly code of the program.
    trace_files : list of file
        List of trace files of the program.
    """

    global start_list
    global end_list

    # Start of a funtion is always the start of a basic block.
    add_item_to_start_list(line_no)

    index = line_no - 1
    while(True):
        index = index + 1

        if (assembly_code[index] == ""):
            # Reached end of the function.
            return

        tokens = assembly_code[index].split()
        # tokens[0] -> address:
        # tokens[1] -> hexadecimal code of machine language instruction
        # tokens[2] -> mnemonic
        # tokens[3] -> operands

        if (len(tokens) < 3):
            # Not a valid instruction. Continue with next line.
            continue

        elif (tokens[2] in branch_inst):
            process_branch_inst(index, tokens, assembly_code)
            
        elif (tokens[2] in jump_inst):
            process_jump_inst(index, tokens, assembly_code, trace_files)
    

def process_branch_inst(line_no: int, tokens: list, assembly_code: list) -> None:
    """Detects basic block starting and end points from given branch instruction.
    
    Processes a given branch instrcution. Depending on the instruction, it
    detects the startng and end points of basic blocks. This is achieved by the 
    help of the rule set.

    This function does not return a value. Instead it adds the line numbers of
    the detected starting and end points of basic blocks to the start_list and
    end_list.

    Parameters
    ----------
    line_no : int
        Line number of the branch instruction which will be processed.
    tokens : list of str
        The branch instruction line which will be processed.
    assembly_code : list of str
        Assembly code of the program.
    """

    operands = tokens[3].split(',')

    # operands[2] -> target address

    target_line_no = asm_tools.address_to_line_no(operands[2], assembly_code)

    # The line of the current branch instruction is the end of a basic block.
    # Branch instructions have two targets.
    # The subsequent line and the branch target are the targets of the branch
    # instruction. We add all this together to the end list.
    add_item_to_end_list(line_no, [line_no + 1, target_line_no])


    # Previous line of the target of a branch instruction is also the end of
    # a basic block.
    add_item_to_end_list(target_line_no - 1)


    # The subsequent line of a branch instruction is the start of basic block.
    add_item_to_start_list(line_no + 1)

    # The target line of a branch instruction is the start of a basic block.
    add_item_to_start_list(target_line_no)


def process_jump_inst(line_no: int, tokens: list, assembly_code: list, 
                      trace_files: list) -> None:
    """Detects basic block starting and end points from given jump instruction.
    
    Processes a given jump instrcution. Depending on the instruction, it
    detects the starting and end points of basic blocks. This is achieved by the 
    help of the rule set.

    This function does not return a value. Instead it adds the line numbers of
    the detected starting and end points of basic blocks to the start_list and
    end_list.

    Parameters
    ----------
    line_no : int
        Line number of the jump instruction which will be processed.
    tokens : list of str
        The jump instruction line which will be processed.
    assembly_code : list of str 
        Assembly code of the program.
    trace_files : list of file
        List of trace files of the program.
    """

    global will_be_visited_fn_list


    if (tokens[2] == 'ret'):
        # If the ret instruction is in the main function then just add that line 
        # the end list. Otherwise do nothing. Because we add other functions'
        # ret instructions to the end list during function call detection in 
        # jal and jalr instructions.
        fn = asm_tools.get_function_name(assembly_code[line_no].split()[0][:-1], assembly_code)
        if (fn == "main"):
            add_item_to_end_list(line_no)

    elif (tokens[2] == 'jal'):
        operands = tokens[3].split(',')

        # operands[1] -> target address
        # Sample code: jal	ra,101c4 <main>
        
        target_line_no = asm_tools.address_to_line_no(operands[1], assembly_code)

        # The line of the jal instruction is the end of a basic block.
        add_item_to_end_list(line_no, [target_line_no])
        
        # Next line of the jal instruction is the start of a basic block. 
        add_item_to_start_list(line_no + 1)

        # Target line of the jal instruction is the start of a basic block.
        add_item_to_start_list(target_line_no)

        # Target of the jal instruction is a function.
        will_be_visited_fn_list.append(target_line_no)

        # Find the end point (ret instruction) of the target function. Its 
        # return point is the next line of the jal instruction. Add this info
        # to the end list.
        # Yelkovan now detects the target of ret instruction
        # by the help of jal instruction in assembly code. Although ret is 
        # a indirect jump instruction there is no need to search for the
        # target of ret instrucion in trace files.
        target_fn = asm_tools.get_function_name(operands[1], assembly_code)
        target_fn_end = asm_tools.get_function_end(target_fn, assembly_code)
        add_item_to_end_list(target_fn_end, [line_no + 1])


    elif (tokens[2] == 'jalr'):

        # tokens[0][:-1] is the address of the jalr instruction.
        target_line_no = find_target(tokens[0][:-1], assembly_code, trace_files)

        if (target_line_no == -1):
            raise Exception("Error: Could not find the target of jalr instruction on line " + line_no)

        # The line of the jalr instruction is the end of a basic block.
        add_item_to_end_list(line_no, [target_line_no])

        # Next line of the jalr instruction is the start of a basic block.
        add_item_to_start_list(line_no + 1)
        
        # Target line of the jalr instruction is the start of a basic block.
        add_item_to_start_list(target_line_no)

        # Target of the jalr instruction is a function.
        will_be_visited_fn_list.append(target_line_no)

        # Find the end point (ret instruction) of the target function. Its 
        # return point is the next line of the jal instruction. Add this info
        # to the end list.
        # Yelkovan now detects the target of ret instruction
        # by the help of jal instruction in assembly code. Although ret is 
        # a indirect jump instruction there is no need to search for the
        # target of ret instrucion in trace files.
        # assembly_code[target_line_no].split()[0][:-1] is the address of the 
        # target line number. get_function_name of asm_tools.py expects address
        # value.
        target_fn = asm_tools.get_function_name(assembly_code[target_line_no].split()[0][:-1], assembly_code)
        target_fn_end = asm_tools.get_function_end(target_fn, assembly_code)
        add_item_to_end_list(target_fn_end, [line_no + 1])


    elif (tokens[2] == 'j'):
        
        # No need to split. Fourth token in the line of a j instruction is
        # the target address
        target_line_no = asm_tools.address_to_line_no(tokens[3], assembly_code)

        add_item_to_start_list(line_no + 1)
        add_item_to_start_list(target_line_no)
        
        add_item_to_end_list(line_no, [target_line_no])
        
        # Previous line of the target of a j instruction is also the end of
        # a basic block.
        add_item_to_end_list(target_line_no - 1)
        

    elif (tokens[2] == 'jr'):

        add_item_to_start_list(line_no + 1)

        target_line_no = find_target(tokens[0][:-1], assembly_code, trace_files)
        if (target_line_no == -1):
            print("Error: Could not find the target of jr instruction on line " + line_no)
        else:
            add_item_to_start_list(target_line_no)
            
            # Previous line of the target of a jr instruction is also the end of
            # a basic block.
            add_item_to_end_list(target_line_no - 1)


        add_item_to_end_list(line_no, [target_line_no])



def find_target(source_address: str, assembly_code: list, 
                trace_files: list) -> int:
    """Finds the line number of the target address of an indirect jump 
    instruction by the help of trace files.
 
    This is achived by processing trace files. Firstly the source address 
    of jump instruction is found in the trace files. The subsequent line  
    is the target of the jump instruction. The address information in the
    subsequent line is extracted. Then, the code line which starts with this
    address is searched in the assembly file. This code line is the target of 
    the jump instruction and the beginning of a basic block. The line number
    of this code line is returned.

    If source address of the jump instruction is not found in the trace files, 
    this means that the path was not taken. In this case an error is raised. The
    error is raised by the "get_next_address" function in the trace_tools file.

    If the target address of the jump instruction is not found the assembly file
    an error is raised. The error is raised by the "address_to_line_no" function 
    in the trace_tools file.

    Parameters
    ----------
    source_address : str
        The source address which will be searched in trace files.
    assembly_code : list of str
        Assembly code in which the line number of the target address will be 
        searched.
    trace_files : list of file
        List of trace files in which the source address will be searched.

    Returns
    -------
    line_no : int
        The line number of the target address. Positive integer if successful,
        raises error otherwise
    """


    target_address = trace_tools.get_next_address(source_address, trace_files)
    line_no = asm_tools.address_to_line_no(target_address, assembly_code)

    return line_no



if __name__ == "__main__":
    """Entry point of the Yelkovan.
    """

    main()