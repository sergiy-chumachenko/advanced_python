from typing import NoReturn, Iterable


# Functions
def nothing(a: int) -> None:
    if a == 1:
        return
    elif a == 2:
        return None
    # elif a == 3:
    #     return ""  # error: No return value expected
    else:
        pass


def forever() -> NoReturn:
    while True:
        pass


def generate_two() -> Iterable[int]:
    yield 1
    yield 2
    #  Incompatible types in "yield" (actual type "str", expected type "int")
    # yield "str"


for i in generate_two():
    print(i)
