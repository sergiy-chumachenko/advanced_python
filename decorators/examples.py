# Examples
import urllib.request as request


def benchmark(func):
    def wrapper(*args, **kwargs):
        import time
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f"{func.__name__, args, kwargs} has called {wrapper.count} times!")
        return res
    wrapper.count = 0
    return wrapper


print('*'*100)


@counter
@benchmark
@logging
def reverse_string(string):
    return string[::-1]


print(reverse_string('Hello World!'))
print('*'*100)


@counter
@benchmark
@logging
def get_random_quote():
    with request.urlopen("https://ru.wikipedia.org") as response:
        the_page = str(response.read(), 'utf-8')
        for word in the_page.split(' '):
            if word.startswith("b"):
                return word
    return "I can't do it!"


print(get_random_quote())
print('*'*100)
