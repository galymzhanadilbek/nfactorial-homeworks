def exercise1():
    print("Exercise 1: Начало")
    num1 = 17
    num2 = 12
    sum = num1 + num2
    print (sum)
    print("Exercise 1: Конец")

def exercise2():
    print("Exercise 2: Начало")
    word = "Breakfast"
    print(word[::-1])
    print("Exercise 2: Конец")

def exercise3():
    print("Exercise 3: Начало")
    word = "Breakfast"
    word_len = len(word)
    print(word_len)
    print("Exercise 3: Конец")

def exercise4():
    print("Exercise 4: Начало")
    word1 = "Break"
    word2 = "fast"
    concatenated_word = word1 + word2
    print(concatenated_word)
    print("Exercise 4: Конец")

def exercise5():
    print("Exercise 5: Начало")
    character = "a"
    vowels = "a, e, i, o, u, y"
    if character in vowels:
        print(f"{character} is a vowel")
    if character not in vowels:
        print(f"{character} is not a vowel")
    print("Exercise 5: Конец")

def exercise6():
    print("Exercise 6: Начало")
    word = "Breakfast"
    first = word[0]
    last = word[-1]
    modified_word = last + word[1:-1] + first
    print(modified_word)
    print("Exercise 6: Конец")

def exercise7():
    print("Exercise 7: Начало")
    word = "Breakfast"
    word_uppercase = word.upper()
    print(word_uppercase)
    print("Exercise 7: Конец")

def exercise8():
    print("Exercise 8: Начало")
    length = 20
    width = 30
    area = length * width
    print(area)
    print("Exercise 8: Конец")

def exercise9():
    print("Exercise 9: Начало")
    num = 20
    if num % 2 == 0:
        print(f"{num} is an even number")
    if num % 2 == 1:
        print(f"{num} is an odd number")
    print("Exercise 9: Конец")

def exercise10():
    print("Exercise 10: Начало")
    word = "Breakfast"
    extracted_word = word[:3]
    print(extracted_word)
    print("Exercise 10: Конец")

def exercise11():
    print("Exercise 11: Начало")
    name = "Jeff"
    age = 21
    print(f"My name is {name} and I am {age} years old.")
    print("Exercise 11: Конец")

def exercise12():
    print("Exercise 12: Начало")
    word = "Breakfast"
    extracted_word = word[2:6]
    print(extracted_word)
    print("Exercise 12: Конец")

def exercise13():
    print("Exercise 13: Начало")
    num = "21"
    converted_num = int(num)
    print(converted_num)
    print("Exercise 13: Конец")

def exercise14():
    print("Exercise 14: Начало")
    word = "Breakfast"
    repeated_word = word * 3
    print(repeated_word)
    print("Exercise 14: Конец")

def exercise15():
    print("Exercise 15: Начало")
    num1 = 21
    num2 = 2
    quotient = 21 // 2
    remainder = 21 % 2
    print(f"quotient: {quotient}\nremainder: {remainder}")
    print("Exercise 15: Конец")

def exercise16():
    print("Exercise 16: Начало")
    num1 = 21
    num2 = 2
    num_divided = num1 / num2
    print(num_divided)
    print("Exercise 16: Конец")

def exercise17():
    print("Exercise 17: Начало")
    word = "Breakfast"
    char_occurance = word.count("a")
    print(char_occurance)
    print("Exercise 17: Конец")

def exercise18():
    print("Exercise 18: Начало")
    word = "Gennady \"GGG\" Golovkin"
    print(word)
    print("Exercise 18: Конец")

def exercise19():
    print("Exercise 19: Начало")
    word = '''Line1
Line2
Line3'''
    print(word)
    print("Exercise 19: Конец")

def exercise20():
    print("Exercise 20: Начало")
    base = 2
    exponent = 3
    result = base ** exponent
    print(result)
    print("Exercise 20: Конец")

def exercise21():
    print("Exercise 21: Начало")
    word = "racecar"
    word_backwards = word[::-1]
    if word == word_backwards:
        print("The word is a palindrome")
    if word != word_backwards:
        print("The word is not a palindrome")
    print("Exercise 21: Конец")

def exercise22():
    print("Exercise 22: Начало")
    word1 = "spar"
    word2 = "rasp"
    if sorted(word1) == sorted(word2):
        print("Positive: anagrams")
    if sorted(word1) != sorted(word2):
        print("Negative: not anagrams")
    print("Exercise 22: Конец")

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()
    exercise18()
    exercise19()
    exercise20()
    exercise21()
    exercise22()