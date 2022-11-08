def str_to_int(string):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    You can pass "1.1" which returns 1
    ["1"] -> raises RuntimeError
    """
    import pdb
    pdb.set_trace()
    error_msg = f"Unable to convert to integer:{string}"

    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    return int(integer)


def str_to_bool(val):
    """
    Convert a string representation of truth to True or False
    True values are 'y', 'yes', or ''; case-insensitive
    False values are 'n', or 'no'; case-insensitive
    Raises ValueError if 'val' is anything else.
    """
    true_vals = ["yes", "y", ""]
    false_vals = ["no", "n"]

    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()

    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError(f"Invalid input value: {val}")


"""
pytest + --pdb(test_file_name.py) opens a debugger in terminal
"""
