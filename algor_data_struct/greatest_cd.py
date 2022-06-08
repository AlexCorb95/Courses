def cmmdc(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

das=cmmdc(121,31)
print(das)