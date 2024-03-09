import unittest
from utils import calculate_average, normalize_numbers

class TestIntegration(unittest.TestCase):
    def test_normalize_numbers(self):
        numbers = [10, 20, 30]
        normalized = normalize_numbers(numbers)
        expected = [-0.5, 0, 0.5]  # Calculado manualmente
        for n, e in zip(normalized, expected):
            self.assertAlmostEqual(n, e)

if __name__ == '__main__':
    unittest.main()