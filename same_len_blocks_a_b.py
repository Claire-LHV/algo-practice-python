def get_number_of_additional_characters(
        s: str,
) -> int:
    previous_char = ''
    number_of_blocks = max_block_len = current_block_len = 0
    for char in s:
        if char != previous_char:
            number_of_blocks += 1
            previous_char = char
            current_block_len = 1
        else:
            current_block_len += 1
        if current_block_len > max_block_len:
            max_block_len = current_block_len
    additional_characters = max_block_len * number_of_blocks - len(s)
    print(additional_characters)
    return additional_characters


get_number_of_additional_characters('babaa')
get_number_of_additional_characters('bbbab')
get_number_of_additional_characters('bbbaaabbb')
get_number_of_additional_characters('ababbbbbba')
get_number_of_additional_characters('aa')
get_number_of_additional_characters('')
get_number_of_additional_characters('bbbbbbbbbbbbbbbba')
