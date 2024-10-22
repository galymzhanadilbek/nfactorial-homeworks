"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n' 
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True
    pass

"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int:
    if n ==0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i -1] + fib[i -2]
    return fib[n]
    pass

"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    nfactorial = 1
    for i in range(2, n + 1):
        nfactorial *= i
    return nfactorial
    pass

"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    vowels = "aeiouy"
    vowels_count = 0
    for letter in s:
        for vowel in vowels:
            if letter == vowel:
                vowels_count += 1
    return vowels_count
    pass

"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(n: int) -> int:
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit
        n = n // 10
    return total_sum
    pass


"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    reversed_s = s[::-1]
    return reversed_s
    pass


"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    total_sum = 0
    squares = 0
    for digit in range(1, n + 1):
        squares = digit ** 2
        total_sum += squares
    return total_sum
    pass


"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    collatz_len = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            collatz_len += 1
        elif n % 2 == 1:
            n = n * 3 + 1
            collatz_len += 1
    return collatz_len + 1
    pass


"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    is_leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False
    return is_leap
    pass


"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    space = " "
    word_count = s.count(space)
    return word_count + 1
    pass


"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    palindrome = False
    if s == s[::-1]:
        return True
    else:
        return False
    pass

"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    multiple = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            multiple += i
    return multiple
    pass


"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    divisors_a = []
    divisors_b = []

    for x in range(1, a + 1):
        if a % x == 0:
            divisors_a.append(x)
    for y in range(1, b + 1):
        if b % y == 0:
            divisors_b.append(y)

    common_divisors = []

    for i in divisors_a:
        if i in divisors_b:
            common_divisors.append(i)
    gcd = max(common_divisors)
    return(gcd)
    pass


"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a: int, b: int) -> int:
    cntr_mltpl_a = 1
    cntr_mltpl_b = 1

    while True:
        mltpl_a = a * cntr_mltpl_a
        mltpl_b = b * cntr_mltpl_b

        if mltpl_a == mltpl_b:
            return(mltpl_a)
            break

        if mltpl_a < mltpl_b:
            cntr_mltpl_a += 1
        else:
            cntr_mltpl_b += 1
    pass


"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""

def count_characters(s: str, c: str) -> int:
    counter_c = 0

    for letter in s:
        if letter == c:
            counter_c += 1
    return counter_c
    pass


"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    counter_n = 0
    for digit in str(n):
        counter_n += 1
    return(counter_n)
    pass


"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    def is_power_of_two(n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 2 == 1:
                return False
            n = n // 2
        return True
    pass


"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    cube_n = []
    for num in range(1, n + 1):
        cube_n.append(num ** 3)

    n_sum = 0
    for i in cube_n:
        n_sum += i
    return(n_sum)

    pass


"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    multiplicator_n = 0
    while multiplicator_n * multiplicator_n < n:
        multiplicator_n += 1
    if multiplicator_n * multiplicator_n == n:
        return True
    else:
        return False
    pass


"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""


def is_armstrong_number(n: int) -> bool:

    cntr_digits = len(str(n))

    n_list = [int(x) for x in str(n)]

    power_sum = sum([digit ** cntr_digits for digit in n_list])

    return power_sum == n
    pass