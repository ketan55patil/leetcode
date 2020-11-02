from romanToInt import roman_to_int
import pytest


class TestRomanToInt:
    @pytest.mark.parametrize('roman_input, int_output',
                             [('III', 3),
                              ('IV', 4),
                              ('IX', 9),
                              ('LVIII', 58),
                              ('MCMXCIV', 1994)])
    def test_roman_to_int(self, roman_input, int_output):
        assert int_output == roman_to_int.roman_to_int(roman_input)
