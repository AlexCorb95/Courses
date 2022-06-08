import unittest
import library


class TestStringMethods(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        f = 32
        c = library.fahrenheit_to_celsius(f)
        self.assertEqual(c, 0)

    def test_cels_to_fharenheit(self):
        c = 0
        f = library.celsius_to_fahrenheit(c)
        self.assertEqual(f, 32)


if __name__ == '__main__':
    unittest.main()
