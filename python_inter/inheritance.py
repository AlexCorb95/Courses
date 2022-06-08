class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        self.color = "white"

    def look(self):
        return "I can see that I have {}".format(self.weight)

    def breath(self):
        pass


class Fish(Animals):
    def __init__(self, weight, age, is_a_swimmer):
        super().__init__(weight=weight, age=age)
        self.swimmer = is_a_swimmer

    def swim(self):
        return self.swimmer


class Bird(Animals):
    def __init__(self, weight, age):
        super().__init__(weight, age)

    def fly(self):
        pass


class Mammal(Animals):
    def __init__(self, weight, age):
        super().__init__(weight, age)

    def run(self):
        pass


class DomesticDog(Mammal):
    has_legs = True

    def __init__(self, weight, age, breed, coat_color, bark_power):
        # super(DomesticDog, self).__init__(weight, age)  # same with -> super().__init__(weight, age)
        super().__init__(weight, age)
        self.object = None
        self.breed = breed
        self.coat_color = coat_color
        self.bark_power = bark_power
        self.a = None
        self.b = 10
        self.c = 10
        self.d = 10

    def bark(self):

        return self.bark_power

    def retrieve(self, object):
        self.object = object
        return self.object


rex = DomesticDog(14, 2, "breed", "orange", 10)
alt_rex = DomesticDog(40, 3, "breed", "yellow", 10)
print(rex.age)
print(rex.a)
rex.age = 3
rex.a = 3
print(rex.age)
print(rex.a)
del rex.a
# print(rex.a)


class Pet(Animals):
    def __init__(self, weight, age, color_of_yes):
        super().__init__(weight, age)
        self.eyesColor = color_of_yes
        self.no_of_eyes = 2


lulu = Pet(3, 0.3, "black")
print(lulu.color)
