from q17_interest import interest

def test_interest():
    result = interest(1000, 10, 2)
    expected = "Simple Interest: 200.0\nCompound Interest: 210.00000000000023"
    assert result == expected
