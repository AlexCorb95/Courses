class Animal:

    def __init__(self, name="", age=0):
        self.name = name  # set the default value for the name field of the Animal class object
        self.age = age

    def print_details(self):  # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}.")


my_dog = Animal(age=1, name="Ursa")
my_dog.print_details()
print(my_dog.name)