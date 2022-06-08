from binary_search import bin_search_ier
import pytest


def test_bin_search():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 4
    c = bin_search_ier(a, b)
    assert b == c
def test_bin_search1():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 6
    c = bin_search_ier(a, b)
    assert b == c
def test_bin_search2():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 0
    c = bin_search_ier(a, b)
    assert False==c
def test_bin_search3():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 12
    c = bin_search_ier(a, b)
    assert False==c
def test_bin_search4():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = 8
    c = bin_search_ier(a, b)
    assert b == c
