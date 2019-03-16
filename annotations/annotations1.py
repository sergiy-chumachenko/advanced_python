# Basics
name: str = 'Mike'
price: int = 10
title: str = 'Post title'

print(name)  # Mike
print(price)  # 10
print(title)  # Post Title


def indent_right(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


string = 'Hello!'
print(indent_right(s=string, width=20))


def hello(username: str) -> None:
    print(f"Hello {username}!")


hello(username=name)
