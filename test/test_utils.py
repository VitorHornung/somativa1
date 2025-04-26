import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_numero_par(self):
        self.assertTrue(utils.eh_par(4))

    def test_numero_impar(self):
        self.assertTrue(utils.eh_par(5))

    def test_zero(self):
        self.assertTrue(utils.eh_par(0))

if __name__ == "__main__":
    unittest.main()