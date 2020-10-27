class LongestSubstring:

    def __init__(self, my_string):
        self.my_string = my_string

    def get_longest_substring(self):
        my_string_list = list(self.my_string)
        longest_string = ''
        index_count = 0
        for char in my_string_list:
            temp_string_list = list()
            temp_string_list.append(char)
            temp_string = ''

            for index in range(index_count+1, len(my_string_list)):
                item = my_string_list[index]
                if item not in temp_string_list:
                    temp_string_list.append(item)
                elif item in temp_string_list:
                    break
                else:
                    print(f'unexpected!!!!!!!')

            temp_string = ''.join(temp_string_list)
            if len(longest_string) < len(temp_string):
                longest_string = temp_string

            index_count = index_count + 1

        return longest_string


if __name__ == '__main__':
    ls = LongestSubstring('pwwkew')
    print(ls.get_longest_substring())
