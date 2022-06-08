

class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass

number_to_compare=10
user_number=int(input("Enter a number:"))

while number_to_compare!= user_number:
    try:
        if number_to_compare>user_number:
            raise ValueTooSmallError

        else:
            raise ValueTooLargeError
    except ValueTooSmallError:
        user_number = int(input("This value is too small, try another number:"))
    except ValueTooLargeError:
        user_number = int(input("This value is too large, try another number:"))
print("Fecilitari, ai ghecit!!")