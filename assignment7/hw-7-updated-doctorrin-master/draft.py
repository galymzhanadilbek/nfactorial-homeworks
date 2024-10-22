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
print(is_perfect_square(9))
