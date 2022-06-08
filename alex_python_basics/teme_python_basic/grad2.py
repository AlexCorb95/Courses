# ecuatie grad 2
import math
print("introdu val a")
a = int(input())
print("introdu val b")
b = int(input())
print("introdu val c")
c = int(input())
delta = b ** 2 - 4 * a * c
print("delta este", delta)
if (delta < 0):
    print("Nu are solutii")
elif (delta == 0):
        x = -b / (2 * a)
        print("X1=X2=", x)
else:
        x = (-b + math.sqrt(delta)) / (2 * a)
        y = (-b - math.sqrt(delta)) / (2 * a)

        print("X1=", x)
        print("X2=", y)
# Sa se scrie o functie care rezolva ecuatia de gradul 2 fiind date a, b, c. Sa se afle x1, x2
def ecuatie_grad2(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - d ** (1 / 2)) / (2 * a)
        x2 = (-b + d ** (1 / 2)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, x

    else:
        return None, None


x1, x2 = ecuatie_grad2(1, 5, 6)
print(x1, x2)
x1, x2 = ecuatie_grad2(1, 2, 1)
print(x1, x2)