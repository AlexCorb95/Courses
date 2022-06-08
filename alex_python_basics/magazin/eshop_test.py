import pytest

from alexandru_corbeanu.alex_python_basics.magazin.magazin import save_products, load_products


def test_save_load_products():
    products=[1,2,3,4]
    save_products(products)
    products_=load_products()
    assert products == products_
