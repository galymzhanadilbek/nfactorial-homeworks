def count_words(s: str) -> int:
    if s == "":
        return 0
    space = " "
    word_count = s.count(space)
    return word_count + 1
print(count_words("word "))
