# import multiprocessing
#
#
# def print_square(number):
#     print(f"Square of {number} is {number ** 2}")
#
#
# def print_cube(number):
#     print(f"Cube of {number} is {number ** 3}")
#
#
# if __name__ == "__main__":
#
#     # create processes
#     p1 = multiprocessing.Process(target=print_square, args=(25,))
#     p2 = multiprocessing.Process(target=print_cube, args=(25,))
#
#     # start process p1
#     p1.start()
#     # start process p2
#     p2.start()
#
#     # wait until process p1 is finished
#     p1.join()
#     # wait until process p2 is finished
#     p2.join()
#
#     print("Execution done")
# ==================================================================================

# import multiprocessing
# import os
#
#
# def worker1():
#     print(f"ID of process running worker1: {os.getpid()}")
#
#
# def worker2():
#     print(f"ID of process running worker2: {os.getpid()}")
#
#
# if __name__ == "__main__":
#     print(f"ID of main process: {os.getpid()}")
#
#     p1 = multiprocessing.Process(target=worker1)
#     p2 = multiprocessing.Process(target=worker2)
#
#     p1.start()
#     p2.start()
#
#     print(f"ID of process p1 is: {p1.pid}")
#     print(f"ID of process p2 is: {p2.pid}")
#
#     print(f"Process p1 is alive: {p1.is_alive()}")
#     print(f"Process p2 is alive: {p2.is_alive()}")
#
#     p1.join()
#     p2.join()
#
#     print(f"Process p1 is alive: {p1.is_alive()}")
#     print(f"Process p2 is alive: {p2.is_alive()}")
# ==================================================================================

# import multiprocessing
#
# result = []
#
#
# def square_list(mylist):
#     global result
#
#     for number in mylist:
#         result.append(number ** 2)
#     print(f"Result in process p1: {result}")
#
#
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5, 6, 7]
#
#     p1 = multiprocessing.Process(target=square_list, args=(my_list,))
#     p1.start()
#     p1.join()
#     print(f"Result in main program: {result}")
# ==================================================================================
import multiprocessing


def square_list(mylist, result, square_sum):
    for i, number in enumerate(mylist):
        result[i] = number ** 2

    # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print(f"Result in process p1 is: {result[:]}")

    # print square_sum Value
    print(f"Sum of squares in process p1 is: {square_sum.value}")


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5, 6, 7]

    # creating Array of in data type with space for 7 integers
    result = multiprocessing.Array("i", 7)

    # creating Value of int data type
    square_sum = multiprocessing.Value("i")

    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    p1.start()

    p1.join()

    print(f"Result in main program is: {result[:]}")
    print(f"Sum of squares in main process is: {square_sum.value}")
