def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_Apples = 0
    count_Oranges= 0

    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            count_Apples +=1
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            count_Oranges +=1
    print(count_Apples)
    print(count_Oranges)

s = 12
t = 15
a = 11
b = 19
apples = [-2,2,3,-3,4,-4]
oranges = [-2,2,3,-3,4,-4]
countApplesAndOranges(s,t,a,b,apples,oranges)