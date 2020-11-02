
def roman_to_int(input_roman):
    # Assign int value to roman chars
    roman_char_val_dict = {'I': 1,
                           'V': 5,
                           'X': 10,
                           'L': 50,
                           'C': 100,
                           'D': 500,
                           'M': 1000}

    input_roman_list = list(input_roman)
    int_value = 0
    prev_char = None

    for index, value in enumerate(input_roman_list):
        cur_char = value

        if (cur_char in ['X', 'V'] and prev_char == 'I') or\
           (cur_char in ['L', 'C'] and prev_char == 'X') or\
           (cur_char in ['D', 'M'] and prev_char == 'C'):
            int_value = int_value + roman_char_val_dict[cur_char] - 2*roman_char_val_dict[prev_char]
        else:
            int_value = int_value + roman_char_val_dict[cur_char]

        prev_char = cur_char
    return int_value


if __name__ == '__main__':
    input_list = ['I', 'III', 'IV', 'IX', 'XX',
                  'LVIII', 'MCMXCIV', 'MMMCMXCIX']

    for item in input_list:
        print(f'Integer value for {item} is {roman_to_int(item)}')

