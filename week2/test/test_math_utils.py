import unittest
from math_utils import multiply

class TestMultiply(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative(self):
        self.assertEqual(multiply(-2, 5), -10)

    def test_zero(self):
        self.assertEqual(multiply(0, 100), 0)

if __name__ == '__main__':
    unittest.main()