

def bin_search_ier(itr, key):
    start = 0
    end = len(itr)-1
    while start <= end:

        mid = (start + end) // 2
        if itr[mid] == key:
            print(f"key is found at index {mid} of list")
            return itr[mid]
        elif itr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    print("key not found")
    return False



if __name__ == '__main__':
    test_lst = [2, 3, 4, 10, 40]
    x = 10
    a = bin_search_ier(test_lst, x)
    print(a)
