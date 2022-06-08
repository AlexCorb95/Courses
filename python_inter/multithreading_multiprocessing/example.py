import timeit
import multiprocessing

def count(_from, _to):
    while _from >= _to:
        _from -= 1


def wo_multiprocessing_func():
    count(40000000, 0)


def with_multiprocessing_func():


    t1 = multiprocessing.Process(target=count, args=(40000000, 20000000))
    t2 = multiprocessing.Process(target=count, args=(20000000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    wo_multiprocessing = "wo_multiprocessing_func()"
    with_multiprocessing = "with_multiprocessing_func()"
    setup = """from __main__ import wo_multiprocessing_func, with_multiprocessing_func
import multiprocessing"""

    print("Without threads:", timeit.timeit(stmt=wo_multiprocessing,
                                       setup=setup,
                                       number=100))
    print("With threads:", timeit.timeit(stmt=with_multiprocessing,
                                         setup=setup,
                                         number=100))