# Methods Decoration
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, variable):
        variable -= 1000  # Try to get more real price
        return method_to_decorate(self, variable)
    return wrapper


class Car:
    def __init__(self, price):
        self.price = price

    @method_friendly_decorator
    def get_real_price(self, variable):
        adjusted = self.price - variable
        return adjusted

    def __str__(self):
        return f"Car Price: {self.price}"


car = Car(1000)
print(car.get_real_price(-250))
