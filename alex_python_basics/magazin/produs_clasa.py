import unittest

from alexandru_corbeanu.alex_python_basics.magazin.produse import Produs


class ProductVerification(unittest.TestCase):
    def setUp(self):
        self.produs = Produs("sapca", 12.5, "accesoriu", 12, "rosie")

    def test_product_update(self):
        # produs=Produs("sapca",12.5,"accesoriu",12,"rosie")
        nume = "tricou"
        self.produs.update(nume=nume)
        self.assertEqual(self.produs.name, nume)

    def test_price_update(self):
        price = 12.55667
        self.produs.update(pret=price)
        self.assertEqual(self.produs.price, 12.56)
