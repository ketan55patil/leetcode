class ConsecutiveCharsCount:
    def count_consecutive_chars(self, str_item: str) -> int:
        max_consecutive_char_count = 0
        prev_char = None
        str_item_list = list(str_item)

        for cur_char in str_item_list:
            # every char will appear at least once
            # so, if prev and cur char is not same then keep the count 1
            cur_consecutive_char_count = (cur_consecutive_char_count + 1 if prev_char == cur_char else 1)

            if cur_consecutive_char_count > max_consecutive_char_count:
                max_consecutive_char_count = cur_consecutive_char_count

            prev_char = cur_char

        return max_consecutive_char_count


if __name__ == '__main__':
    obj_ccc = ConsecutiveCharsCount()
    str_list = ['hi', 'hello']
    for my_str_item in str_list:
        cons_char_count = obj_ccc.count_consecutive_chars(my_str_item)
        print(f'Consecutive char count for {my_str_item} is {cons_char_count}')
