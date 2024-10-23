def find_union(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 | set2)
print(find_union([1,2,3,4,5],[2,3,4,5,6]))



