# Fibonacci number https://en.wikipedia.org/wiki/Fibonacci_number
# With Recursion


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))


# Functional
def fib_func(n):
    i, a = 0, 0
    b = 1
    while i != n-1:
        a, b = b, a+b
        i += 1
    return b


print(fib_func(10))


# FibonacciNumber Iterator

class FibonacciNumber:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return FibonacciNumberIterator(self.a, self.b)


class FibonacciNumberIterator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value


fib = FibonacciNumber()
print(fib)  # <__main__.FibonacciNumber object at 0x7f29c760def0>
print(type(fib))  # <class '__main__.FibonacciNumber'>
fib = fib.__iter__()
print(fib)  # <__main__.FibonacciNumberIterator object at 0x7f25efa85f60>
print(type(fib))  # <class '__main__.FibonacciNumberIterator'>

for i in range(11):
    print(fib.__next__())
