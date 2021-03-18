""" Test the functionality of asm_tools.py

This program tests the following functions of asm_tools.py

get_function_name
get_function_start
get_function_end

"""


# This file tests asm_tools.py
import asm_tools


def main(file_name: str):
    """Main function of this test program.

    This function does not return a value.


    Parameters
    ----------
    file_name : str
        The name of the assembly file to be tested.
    """

    content: list = None
    fn_name: str = None
    fn_starting_point: int = -1
    fn_end_point: int = -1


    with open(file_name) as f:
        content = f.read()
    f.closed
    
    assembly_code = content.splitlines()
    
    # Test get_function_name
    fn_name = asm_tools.get_function_name("1019c", assembly_code)
    print(f"Expected function name: calc. Function start address \"1019c\". "
          f"Found function name: {fn_name}.")
    
    # Test get_function_start
    fn_starting_point = asm_tools.get_function_start(fn_name, assembly_code)
    print(f"Function \"calc\". Expected starting point of function: 97. " 
          f"Found starting point of function: {fn_starting_point}.")

    # Test get_function_end
    fn_end_point = asm_tools.get_function_end(fn_name, assembly_code)
    print(f"Function \"calc\". Expected end point of function: 112. "
          f"Found end point of function: {fn_end_point}.")    

    # Test error string of get_function_name
    fn_name = asm_tools.get_function_name("200000", assembly_code)
    print(f"Function should not be found on address \"200000\".")


if __name__ == "__main__":
    """Entry point of the program.

    This test pogram tests asm_tools with the loop_test.dump file.
    """

    file_name: str = "test_data/loop_test.dump"

    print(f"The name of the assembly file to be tested is: {file_name}")

    main(file_name)