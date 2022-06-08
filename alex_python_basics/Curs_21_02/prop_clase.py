class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


my_dog = Animal("Dog", 11)
my_dog.name = "Rex"  # Sets age - uses setter
print(my_dog.name)  # Reads age - uses a getter
