# Decorators with arguments
def decorator_maker(dec_arg1=None, dec_arg2=None):
    print("I create decorator!")
    print(f"I got arguments for decorator: {dec_arg1} and {dec_arg2}")

    def my_decorator(decorated_func):
        print("I'am a decorator!")
        print(f"You could send decorator args to decorator: {dec_arg1} and {dec_arg2}")

        def wrapper(func_arg1=None, func_arg2=None):
            print("I'm a wrapper")
            print(f"I got access to:\n"
                  f"\t1) decorator args: {dec_arg1} and {dec_arg2} \n"
                  f"\t2) function args: {func_arg1} {func_arg2}")
            decorated_func(func_arg1, func_arg2)
        return wrapper
    return my_decorator


def decorated_function(func_arg1=None, func_arg2=None):
    print("I'm a decorated function")


new_decorator = decorator_maker()
decorated_function = new_decorator(decorated_function)
decorated_function()
decorated_function = decorator_maker()(decorated_function)
decorated_function()


print('*'*100)


@decorator_maker(dec_arg1="Dec Arg#1", dec_arg2="Dec Arg#2")
def decorated_func_2(dec_arg1=None, dec_arg2=None):
    print("I'm a decorated function #2")


decorated_func_2()


print('*'*100)
d_arg1 = "Decorator Arg#1"
d_arg2 = "Decorator Arg#2"

f_arg1 = "Function Arg#1"
f_arg2 = "Function Arg#2"


@decorator_maker(dec_arg1=d_arg1, dec_arg2=d_arg2)
def decorated_func_3(func_arg1=None, func_arg2=None):
    print("I'm a decorated function #3")
    print("I got access to function args:\n"
          f"\t1) function args: {func_arg1} {func_arg2}")
    print("I'm very happy!")


decorated_func_3(f_arg1, f_arg2)
