def factorial(numar_maxim):
    if numar_maxim < 0:
        return None

    elif numar_maxim == 1 or numar_maxim == 0:
        return 1
    else:
        return numar_maxim * factorial(numar_maxim - 1)


if __name__ == '__main__':
    print(factorial(5))
