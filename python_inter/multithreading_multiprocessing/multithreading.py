# import threading


# def print_square(number):
#     print(f"Square of {number} is {number ** 2}")


# def print_cube(number):
#     print(f"Cube of {number} is {number ** 3}")


# if __name__ == "__main__":
#     t1 = threading.Thread(target=print_square, args=(20,))
#     t2 = threading.Thread(target=print_cube, args=(20,))

#     # start thread t1
#     t1.start()
#     # start thread t1
#     t2.start()

#     # wait until thread t1 was completely executed
#     t1.join()
#     # wait until thread t2 was completely executed
#     t2.join()

#     print("Execution done")
# ==================================================================================

# import threading
# import os


# def task1():
#     print(f"Task 1 assigned to thread: {threading.current_thread().name}")
#     print(f"ID of process running task 1: {os.getpid()}")


# def task2():
#     print(f"Task 2 assigned to thread: {threading.current_thread()}")
#     print(f"ID of process running task 2: {os.getpid()}")


# if __name__ == "__main__":
#     print(f"ID of process running main program is: {os.getpid()}")
#     print(f"Main thread name is: {threading.current_thread().name}")

#     create threads
#     t1 = threading.Thread(target=task1, name="Task T1")
#     t2 = threading.Thread(target=task2, name="Task T2")

#     start threads
#     t1.start()
#     t2.start()

#     wait untill all threads finish
#     t1.join()
#     t2.join()
# ==================================================================================

# import threading

# a = 0
# # i = 0


# def increment():
#     global a
#     a += 1


# def thread_task():
#     # global i
#     for i in range(100000):
#         increment()

# # print(i)

# def main_task():
#     global a
#     a = 0

#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()


# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print(f"Iteration {i}: a = {a}")

# ==================================================================================
# import threading

# a = 0
# i = 0


# def increment():
#     global a
#     a += 1


# def thread_task(lock):
#     global i
#     for i in range(100000):
#         lock.acquire()
#         increment()
#         lock.release()

# print(i)

# def main_task():
#     global a
#     a = 0

#     lock = threading.Lock()

#     t1 = threading.Thread(target=thread_task, args=(lock,))
#     t2 = threading.Thread(target=thread_task, args=(lock,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()


# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print(f"Iteration {i}: a = {a}")
