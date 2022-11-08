def str_to_int(string):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    You can pass "1.1" which returns 1
    ["1"] -> raises RuntimeError
    """
    error_msg = "Unable to conver to integer:'%s'" % str(string)

    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    return int(integer)

