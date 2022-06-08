def password_verification():
    pas = int(input("Enter code:"))
    if pas == 854:
        return print("Code accepted")
    else:
        password_verification()


ver = password_verification()
