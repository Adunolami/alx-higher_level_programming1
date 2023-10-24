#!/urs/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an interger with "{:d}".format().

    if a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The interger to print.

    Return:
        if a  TypeError or ValueError occurs - false.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]). file-sys.stderr)
        return (False)
