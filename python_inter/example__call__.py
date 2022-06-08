# object() -- object.__call__()

class Example:
    def __init__(self):
        print("Instance was created")

    def __call__(self):
        print("Instance is called via special method")


# Instance ex was created
ex = Example()
ex()


class Product:
    def __init__(self):
        print("Instance was created")

    def __call__(self, a, b):
        print(a + b)


# x = Product()
#
# x(2, 7)
