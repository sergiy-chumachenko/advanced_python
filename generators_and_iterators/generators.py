"""
Генераторы

Генераторы позволяют значительно упростить работу по конструированию итераторов. В предыдущих примерах, для построения
итератора и работы с ним, мы создавали отдельный класс. Генератор – это функция, которая будучи вызванной в функции
next() возвращает следующий объект согласно алгоритму ее работы. Вместо ключевого слова return в генераторе используется
yield.
"""
# Generator expression
exp = (x for x in range(10))
print(exp)  # <generator object <genexpr> at 0x7f4f41942938>
print(type(exp))  # <class 'generator'>

print('*'*50)


# Generator object
def simple_generator(val):
    while val > 0:
        val -= 1
        yield val


gen = simple_generator(10)  # Create Generator
print(gen)  # object simple_generator at 0x7f91294cc830>
print(type(gen))  # <class 'generator'>
for elem in gen:
    print(elem)  # 9, 8, 7, 6 ...

# Can be used only one time
print('*'*50)
gen2 = simple_generator(10)  # Create Generator
print(next(gen2))  # 9, 8, 7, 6 ...
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print('*'*50)

gen3 = (num*2 for num in range(10))
for _ in range(10):
    print(gen3.__next__())
