# Basic Built-in types

from typing import Optional, Any, Union

amount: int = 100
# -> error: Incompatible types in assignment (expression has type "None", variable has type "int")
# amount = None


'''
An optional type annotation is provided in the typing module indicating the specific type Union[X, None]. 
'''
price: Optional[int]
price = None
print(price)

'''
Sometimes you don’t want to limit the possible types of a variable. 
For example, if it is really not important, or if you plan to do the 
processing of different types on your own. In this case, you can use the Any annotation.
'''
unknown_item: Any = 1
print(unknown_item)
# print(unknown_item.startwith("Hello"))
# print(unknown_item // 0)

'''
For cases where it is necessary to allow the use of not any type, but only some, 
you can use typing.Union annotation with the list of types in square brackets.
'''


def hundreds(x: Union[int, float]):
    return (int(x) // 100) % 10


print(hundreds(100.0))
print(hundreds(100))
print(hundreds("100"))  # Argument 1 to "hundreds" has incompatible type "str"; expected "Union[int, float]"

