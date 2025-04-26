import unittest
from calculadora import somar, subtrair

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(0, 3), -3)

if __name__ == '__main__':
    unittest.main()
