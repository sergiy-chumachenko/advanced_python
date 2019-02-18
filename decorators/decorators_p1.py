"""
Декораторы — это, по сути, просто своеобразные «обёртки», которые дают нам возможность делать что-либо до и после того,
что сделает декорируемая функция, не изменяя её.
"""


def my_new_decorator(func_to_decorate):
    def wrapper_around_original_function():
        print("I'm code which works before original function")
        func_to_decorate()
        print("I'm code which works after original function")
    return wrapper_around_original_function


def original_function():
    print("I'm original function")


original_function()

print('*'*100)
original_function = my_new_decorator(original_function)
original_function()
print('*'*100)


@my_new_decorator
def original_function():
    print("I'm original function")


original_function()
print('*'*100)
