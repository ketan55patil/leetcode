# from longestSubstring import longest_substring as ls
import longest_substring as ls


class TestLongestSubstring:

    def test_get_longest_substring(self):

        test_strings_dict = {'a': 'a', 'ab': 'ab', 'pwwkew': 'wke',
                             'pwwkewa': 'kewa', 'abcabc': 'abc', 'bbbb': 'b'}

        for k, v in test_strings_dict.items():
            obj_ls = ls.LongestSubstring(k)
            assert v == obj_ls.get_longest_substring()


obj_tls = TestLongestSubstring()
obj_tls.test_get_longest_substring()

# to execute this run following in the terminal
# pipenv run pytest test_first_test.py::TestLongestSubstring
