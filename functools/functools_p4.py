from functools import partial

my_bin = partial(int, base=2)
print(my_bin('1111'))  # 15


def my_func(a, b):
    if a > b:
        return b
    return a


my_new_func = partial(my_func, b=100)
print(my_new_func(10))  # 10
print(my_new_func(1000))  # 1000
