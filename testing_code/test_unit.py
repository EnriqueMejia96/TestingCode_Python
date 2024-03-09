import unittest
from utils import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_with_positive_numbers(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)
   
    def test_with_negative_numbers(self):
        self.assertEqual(calculate_average([-10, -20, -30]), -20)

if __name__ == '__main__':
    unittest.main()