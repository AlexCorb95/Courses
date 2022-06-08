# Fiind dat un user care are proprietatea booleana autentificat, sa se scrie un decorator care permite executia functiei
# doar daca userul este autentificat.
class NotLoggedIn(Exception):
    pass


class User:
    def __init__(self, autentificat):
        self.autentificat = autentificat


eu = User(True)


def verify_auth(func):
    def inner():
        if eu.autentificat:
            result = func()
            return result
        else:
            raise NotLoggedIn

    return inner


@verify_auth
def print_to_10():
    print([i for i in range(11)])

print_to_10()
