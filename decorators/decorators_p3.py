# Give arguments to the decorated function
def my_decorator(func):
    def wrapper(*args):
        print(f"Look what I get: {args}")
        func(*args)
    return wrapper


@my_decorator
def original_function(first_name, last_name):
    print(f"My name is: {first_name} {last_name}")


original_function('John', 'Smith')
