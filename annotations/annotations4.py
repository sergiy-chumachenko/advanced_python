from typing import List, Dict, Tuple

'''
Collections
The type annotation mechanism supports the generics mechanism (Generics), 
which allow specifying types of elements stored in containers for containers.
'''

# Lists
titles: List[str] = ["hello", "world"]
# titles.append(100500)  # Argument 1 to "append" of "list" has incompatible type "int"; expected "str"

# titles = ["hello", 1]  # List item 1 has incompatible type "int"; expected "str"

items: List = ["Hello", 1]  # Everything is OK!

# Tuples
price_container: Tuple[int] = (1,)

# Incompatible types in assignment (expression has type "Tuple[str]", variable has type "Tuple[int]")
# price_container = ("hello",)

# Incompatible types in assignment (expression has type "Tuple[int, int]", variable has type "Tuple[int]")
# price_container = (1, 2)

price_with_tuple: Tuple[int, str] = (1, "hello")

prices: Tuple[int, ...] = (1, 2)  # OK
prices = (1,)  # OK

#  Incompatible types in assignment (expression has type "Tuple[int, str]", variable has type "Tuple[int, ...]")
# prices = (1, "hello")

something: Tuple = (1, 2, "hello", "hi")  # OK

# Dictionaries
book_authors: Dict[str, str] = {"Fahrenheit 451": "Bradbury"}  # OK

# Incompatible types in assignment (expression has type "int", target has type "str")
# book_authors["1984"] = 0

# Invalid index type "int" for "Dict[str, str]"; expected type "str"
# book_authors[1984] = "Orwell"
