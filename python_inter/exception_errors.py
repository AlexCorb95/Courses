# create a function that has 2 parameters : balance, and  withdrawal amount
# the function prints withdrawal amount and the new balance

# create decorators : curs_euro si curs_usd, 4.95 per euro, 4.5 per usd

# 1 decorate function using a function decorator
# 2 decorate a class using a function decorator
# 3 decorate a class using a class decorator
def curs_euro(func):
    def inner(balance, withdraw):
        euro_balance = (balance-withdraw)/4.95
        euro_withdraw = withdraw / 4.95
        print(f"the balance is {balance-withdraw}, in euro is {euro_balance}")
        print(f"the withdraw is {withdraw}, in euro is {euro_withdraw}")

        return func(balance, withdraw)

    return inner

    # func = func / 4.95
    # print(f"Your amount in euro is {func}")


def curs_usd(func):
    def inner(balance, withdraw):
        euro_balance = (balance - withdraw) / 4.5
        euro_withdraw = withdraw / 4.5
        print(f"the balance is {balance - withdraw}, in usd is {euro_balance}")
        print(f"the withdraw is {withdraw}, in usd is {euro_withdraw}")

        return func(balance, withdraw)

    return inner


@curs_usd
@curs_euro
def lucram_la_nume(balance, withdraw):
    # withdraw = int(input("State the amount you want to withdraw:"))
    new_balance = balance - withdraw
    print(f"You withdraw {withdraw}")
    print(f"Your new balance is {new_balance}")


x = lucram_la_nume(2000, 100)


