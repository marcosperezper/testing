def test_long_dictionaries():
    result = {'key': 'value', 'lastname': 'perez', 'name': 'marcos'}
    expected = {'key': 'value', 'lastname': 'perez', 'name': 'marcos'}
    assert result == expected
