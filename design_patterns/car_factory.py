# 1. Sa se scrie un factory method care produce un numar variabil de masini de culori random.
# Car: color, body, price
import random


class Car:
    def __init__(self, body, price, color):
        self.body = body
        self.price = price
        self.color = color

    def __repr__(self):
        return f" {self.body} price {self.price} color {self.color}"


def random_car():
    color_lst = ["red", "black", "blue"]
    body_lst = ["Sedan", "hatchback", "sport", "off_road"]
    random_body = body_lst[random.randint(0, len(body_lst) - 1)]
    random_color = color_lst[random.randint(0, len(color_lst) - 1)]
    return Car(random_body, random.randint(15000, 60000), random_color)


""""Factory function list"""


def car_factory(car_count):
    cars = []
    for i in range(1, car_count + 1):
        cars.append(random_car())
    return cars


"""Generator function"""


def car_factory_generator(car_count):
    for i in range(1, car_count + 1):
        yield random_car()

# pprint.pprint(car_generator(100))

# t1=time.time()
# car_factory(1000000)
# t2=time.time()
# car_factory_generator(1000000)
# t3=time.time()
# print(t2-t1)
# print(t3-t2)
