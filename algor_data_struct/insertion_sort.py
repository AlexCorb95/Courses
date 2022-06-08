def insertion_sort(array,ascending=True):

    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        # condition =array[j] > key_item if ascending else array[j] < key_item
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

a=[1,4,7,8,3,2,6]
insertion_sort(a)
print(a)