import pytest

from pythonTDD.Curs09_03 import library


def test_fahrenheit_to_celsius():
    f = 32
    c = library.fahrenheit_to_celsius(f)
    assert c==0


def test_cels_to_fharenheit():
    c = 0
    f = library.celsius_to_fahrenheit(c)
    assert f==32
