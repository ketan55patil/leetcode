import pytest
from consecutiveChars import conscutive_chars_count as cc


class TestConsecutiveCharsCount:
    @pytest.mark.parametrize('input_str, output_count',
                             [('leetcode', 2),
                              ('abbcccddddeeeeedcba', 5),
                              ('triplepillooooow', 5),
                              ('hooraaaaaaaaaaay', 11),
                              ('tourist', 1)])
    def test_count_consecutive_chars(self, input_str, output_count):
        print(type(input_str))
        assert output_count == cc.ConsecutiveCharsCount.count_consecutive_chars(self, input_str)
