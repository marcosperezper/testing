long_string = "This is a very long string that needs to be compared."


def test_long_string():
    expected = "This is A very long string that needs to be compared."
    assert long_string == expected
