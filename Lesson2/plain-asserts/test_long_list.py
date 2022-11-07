def test_long_list():
    result = ["This","is","a","list","with", "a", "lot", "of", "items"]
    expected =  ["This","is","an","list","with", "a", "lot", "of", "items"]
    assert result == expected