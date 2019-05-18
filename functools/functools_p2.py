from functools import cmp_to_key
from random import randint


def func(elem1, elem2):
    if elem1 > elem2:
        return 1
    elif elem1 < elem2:
        return -1
    return 0


lst = [randint(1, 1000) for num in range(100)]
sorted_lst = sorted(lst, key=cmp_to_key(func))
print(sorted_lst)
