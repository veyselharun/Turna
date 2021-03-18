"""Assembly tools of Yelkovan.

This file includes helper functions to process assembly file.


"""


def get_function_start(function_name: str, assembly_code: list) -> int:
    """Detects the line number of the first instruction of a function.

    Searches for a function which is named with the parameter `function_name` in 
    the assembly code. After finding the function returns the line number of the 
    first instruciton of the function.
    
    The presence of "<function_name>:" expression in a line indicates the start 
    of the function. The next line is the first instruction line of that 
    function.

    Parameters
    ----------
    function_name : str
        The name of the function which will be searched in the assembly code.
    assembly_code : list of str
        Assembly code in which the main function will be searched.
    
    Returns
    -------
    integer
        The line number of the of the first instruction of the funtion in the
        assembly code if successful.
    
    Raises
    ------
    Exception
        If the function is not found in the assembly code.
    """

    line_no: int = -1
    function_declaration:str = '<' + function_name + '>:'

    for index, line in enumerate(assembly_code):
        if function_declaration in line:
            line_no = index
            break

    if line_no == -1:
        raise Exception("The function" + function_name + "could not be found "
                        "in the current assembly code.")
    else:
        return line_no + 1



def get_function_end(function_name: str, assembly_code: list) -> int:
    """Detects and returns the line number of the last instruction of a function.

    Searches for a function which is named with the parameter `function_name` in 
    the assembly code. After finding the function returns the line number of the 
    last instruciton of the function.
    
    The presence of "<function_name>:" expression in a line indicates the start 
    of the function. The line which includes "ret" instruction is the last 
    instruction line of the function.

    Parameters
    ----------
    function_name : str
        The name of the function which will be searched in the assembly code.
    assembly_code : list of str
        Assembly code in which the main function will be searched.
    
    Returns
    -------
    integer
        The line number of the last instruction of the funtion in the
        assembly code if successful.
    
    Raises
    ------
    Exception
        If the function is not found in the assembly code or if the "ret"
        instruction in the function is not found.
    """


    found = False
    start_no = get_function_start(function_name, assembly_code)

    line_no = start_no - 1
    for line in assembly_code[start_no:]:
        line_no = line_no + 1
        
        # If an empty line is found this means that the end of the function is 
        # reached and no ret instruction is encountered
        if (line == ''):
            break
        
        # Tokenize the current line and check if it is ret instruction or not.
        tokens = line.split()
        if (len(tokens) >= 3 and tokens[2] == 'ret'):
            found = True
            break


    if found == True:
        return line_no
    else:
        raise Exception("The end point of the function" + function_name + "could "
                        "not be found in the current assembly code.")



def address_to_line_no(address: str, assembly_code: list) -> int:
    """Finds the line number of an address.

    Converts the address information to line number. Expected address 
    information is in bare hexadecimal format without any 0x, h, etc. extension.
    A sample address is "101e8". This address information is the first value
    of each instruction line in assembly code of the program.

    The addresses in assembly code ends with colon symbol (:). A sample first 
    value in of instruction line is "101c4:". Therefore, during extaction of
    this value from the instruction line, colon symbol is discarded.

    Parameters
    ----------
    address : str
        The address whose line number will be searched.
    assembly_code : list of str
        Assembly code in which the address will be searched.

    Returns
    -------
    int
        The line number of the of the address if successful.
    
    Raises
    ------
    Exception
        If the address is not found in the assembly code.
    """

    line_no: int = -1
    found: bool = False

    for index, line in enumerate(assembly_code):
        tokens = line.split()
        # If len(tokens >=3) this is a valid code line.
        # -1 is to discard the colon symbol (:) at the end of the token.
        if len(tokens) >= 3 and tokens[0][:-1] == address:
            line_no = index
            break

    if line_no == -1:
        raise Exception("The address could not be found in the current assembly "
                        "file. The line number of address could not be "
                        "determined. Address: " + address)
    else:
        return line_no


def get_function_name(address: str, assembly_code: list) -> str:
    """Detects the name of a function.

    Detects the name of the function that includes the address which is passed
    as argument. Expected address information is in bare hexadecimal format 
    without any 0x, h, etc. extension. A sample address is "101e8".

    This function first gets the line number of the address. Then it processes
    the assembly code backwards and looks for the template of function start
    line. A sample function start line is like "000000000001019c <calc>:". It
    looks for the ">:" symbols at the end of the line. When found it extracts
    the string inside angle brackets (< and >). This is the function name.

    Parameters
    ----------
    address : str
        The address of the code line whose function will be searched.
    assembly_code : list of str
        Assembly code in which the function name will be searched.

    Returns
    -------
    str
        The name of the function which includes the address.
    
    Raises
    ------
    Exception
        If the function name is not found in the assembly code.
    """

    function_name: str = None
    line_no: int = -1

    line_no = address_to_line_no(address, assembly_code)
    if line_no == -1:
        raise Exception("Line number of the address can not be determined. Address: " + address)

    for i in range(line_no, -1, -1):
        tokens = assembly_code[i].split()
        if (len(tokens) == 2) and (">:" in tokens[1]):
            function_name = tokens[1][1 : -2]
            break

    if function_name is None:
        raise Exception("Function name can not be determined. Address: " + address)
    else:
        return function_name