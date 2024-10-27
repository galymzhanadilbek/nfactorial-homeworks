def char_frequency(my_string: str) -> dict:
    occ_count = dict()
    for letter in my_string:
        count = my_string.count(letter)
        occ_count.update({letter: count})

    return occ_count


def least_frequent(my_list: list) -> int:
    for num in my_list:
        count = my_list.count(num)
        if count == 1:
            return num

print(least_frequent([1]))



