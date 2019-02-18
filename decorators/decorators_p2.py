# Make a Sandwich with the help of decorators
def bread(func):
    def wrapper():
        print("|---bread---|")
        func()
        print("|---bread---|")
    return wrapper


def ingredients(func):
    def wrapper():
        print('|~~tomates~~|')
        func()
        print('|~~~salad~~~|')
    return wrapper


def cheese(func):
    def wrapper():
        print('|===cheese==|')
        func()
    return wrapper


@bread
@ingredients
@cheese
def func():
    print('|~~~~meat~~~|')


print("Our Sandwich has ready")
print('-'*50)
func()  # Our Sandwich has ready
