"""Trace tools of Yelkovan.

This file includes helper functions to process trace file.


"""


def get_next_address(address: str,  trace_files: list) -> str:
    """Detects the line which includes the address. Then returns the 
    address of the following line in trace file.

    """


    for file in trace_files:

        with open(file) as f:
            content = f.read()
        f.closed

        trace_content = content.splitlines()

        for line_no, line in enumerate(trace_content, 0):
            tokens = line.split()
            # If len(tokens) >= 4 means this a valid trace line.
            if len(tokens) >= 4 and tokens[4][2:] == address:
                tokens_target = trace_content[line_no + 1].split()
                return tokens_target[4][2:]

    raise Exception('The address could not be found in the trace files.')              
