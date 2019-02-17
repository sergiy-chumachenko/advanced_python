"""
Итератор – любой объект, реализующий метод __next__, который возвращает следующий элемент в очереди или выбрасывает
исключение StopIteration, если не осталось элементов.

Итерируемый объект – любой объект, реализующий метод __iter__ или __getitem__.
Итерируемым объектом является любая коллекция: список, кортеж, словарь, и т.д.

Цель итерируемого объекта – создать итератор. Для этого у него есть метод __iter__, при каждом обращении к которому
создается новый итератор.

Цель итератора – пройтись по элементам. Для этого у него есть метод __next__, который возвращает элементы один
за другим.

Если итератор реализует метод __iter__ или __getitem__, дополнительно к методу __next__, то он также является и
итерируемым объектом. Это позволяет использовать итератор там, где требуется итерируемый объект.
"""
# Simple for loop
items = [1, 2, 3, 4, 5]
# for elem in items:
#     print(elem)

it = iter(items)  # Get Iterator
print(type(it))  # <class 'list_iterator'>
while True:
    try:
        print(it.__next__())
    except StopIteration:
        break


#  Design Patterns (Iterator)
class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return SquareIterator(self.start, self.stop)


class SquareIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


square_iterator = Squares(10, 20).__iter__()
print(square_iterator.__next__())
print(square_iterator.__next__())
print(square_iterator.__next__())
print(square_iterator.__next__())


class CubeVolume:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return CubeVolumeIterator(self.start, self.stop)


class CubeVolumeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start**3
        self.start += 1
        return current


cube_iterator = CubeVolume(1, 5).__iter__()
print(cube_iterator.__next__())
print(cube_iterator.__next__())
print(cube_iterator.__next__())
print(cube_iterator.__next__())


iter_obj = CubeVolume(10, 15)
print(type(iter_obj))  # <class '__main__.CubeVolume'>
print(type(iter_obj.__iter__()))  # <class '__main__.CubeVolumeIterator'>
for elem in iter_obj:
    print(f'Volume = {elem}')

