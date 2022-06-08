def pageCount(n, p):
    first=p//2
    last=(n-p)//2
    if p==1:
        return 0
    elif n-p==1 and n%2==0:
        return 1
    else:
        return min(first,last)
print(pageCount(2,1))