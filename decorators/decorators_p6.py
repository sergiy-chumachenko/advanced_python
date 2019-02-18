# Decorators for decorators


def decorator_with_args(decorated_decorator):
    print("I'm a decorator for decorators!")

    def decorator_maker(*args, **kwargs):
        print("I create the decorators")

        def decorator_wrapper(func):
            print("I'm a decorator wrapper function!")
            return decorated_decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    print("I'm a decorated decorator!")
    print(f"I have got arguments:\n1){args}\n2){kwargs}")

    def wrapper(func_args1=None, func_args2=None):
        print("I'm wrapper!")
        print(f"I have got function's arguments: {func_args1} and {func_args2}")
        print(f"I have got decorator's arguments: {args} and {kwargs}")
        return func(func_args1, func_args2)
    return wrapper


@decorated_decorator(1, 2, 3, {'a': 1, 'b': 2, 'c': 3}, d=5, f=6, h=7)
def decorated_function(f_args1=None, f_args2=None):
    print(f"I'm a decorated function decorated by decorated decorator :)")
    print(f"I have got arguments: {f_args1} and {f_args2} ")
    print('Goodbye!')


decorated_function('A', 'B')
