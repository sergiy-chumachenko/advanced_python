from functools import total_ordering


@total_ordering
class Book(object):
    def __init__(self, title, pages):
        self.pages = pages
        self.title = title

    def __lt__(self, other):
        return self.pages < other.pages


b1 = Book('Harry Poter', 1000)
b2 = Book('Hobbit', 1001)

print(b1 < b2, b1 > b2, b1 == b2, b1 != b2)
