from q1_temperature import celsius_to_fahrenheit

def test_temperature():
    result = celsius_to_fahrenheit(0)
    expected = "Celsius: 0\nFahrenheit: 32.0"
    assert result == expected
