import unittest
# from longestSubstring import longest_substring as ls
import longest_substring as ls


class TestLongestSubstring(unittest.TestCase):

    def test_get_longest_substring(self):

        test_strings_dict = {'': '', 'a': 'a', 'ab': 'ab', 'pwwkew': 'wke',
                             'pwwkewa': 'kewa', 'abcddeefgh': 'abcd', 'bbbb': 'b'}

        for k, v in test_strings_dict.items():
            obj_ls = ls.LongestSubstring(k)
            self.assertEqual(v, obj_ls.get_longest_substring())


if __name__ == '__main__':
    unittest.main()
# to execute this run following in the terminal
# pipenv run python test_first_unit_test.py
