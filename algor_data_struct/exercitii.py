#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     points_a=0
#     points_b=0
#     index=0
#     while index < len(a) :
#         if a[index] > b[index]:
#             points_a+=1
#         elif a[index] < b[index]:
#             points_b+=1
#         index+=1
#     if points_a > points_b:
#         lst1=[points_a,points_b]
#         return lst1
#     else:
#         lst2=[points_b,points_a]
#         return lst2
#
# if __name__ == '__main__':
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
#     result = compareTriplets(a, b)
#
#     print(' '.join(map(str, result)))
#
def plusMinus(arr):
    poz_val = 0
    neg_val = 0
    prop_zero = 0
    for char in arr:
        if char > 0:
            poz_val += 1
        elif char < 0:
            neg_val += 1
        else:
            prop_zero += 1
    poz_val = poz_val / len(arr)
    neg_val = neg_val / len(arr)
    prop_zero = prop_zero / len(arr)
    return poz_val,neg_val,prop_zero
ar=[-4, 3, -9, 0, 4, 1]
print(plusMinus(ar))