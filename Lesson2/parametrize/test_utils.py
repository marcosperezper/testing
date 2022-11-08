import pytest


from utils import str_to_bool

"""
The functions are separated becasue is not a good practice to do a for loop in a unit test,
 because the failures don't show ever single iteration of the loop.
 The loop stops in the first fail and don't show all of the values.
 """


# def test_yes_is_true():
#     result = str_to_bool("yes")
#     assert result is True
    
# def test_y_is_true():
#     result = str_to_bool("y")
#     assert result is True


@pytest.mark.parametrize('value',["No","N"])
def test_is_true(value):
    result = str_to_bool(value)
    assert result is False


@pytest.mark.parametrize('value',["yes","y",""])
def test_is_false(value):
    result = str_to_bool(value)
    assert result is True