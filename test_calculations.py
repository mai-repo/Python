# Create a separate file for your unit tests (e.g., test_calculations.py). In this file, import the functions you defined and write unit tests for each function. Here's an example structure:
      
import unittest
from first_assignment import subtrate_numbers, divide_numbers

class TestCalculations(unittest.TestCase):
        def test_add_numbers(self):
                self.assertEqual(subtrate_numbers(5, 3), 2)
                self.assertEqual(subtrate_numbers(1, 1), 0)

        def test_multiply_numbers(self):
                self.assertEqual(divide_numbers(10, 5), 2)
                self.assertEqual(divide_numbers(20, 2), 10)

if __name__ == '__main__':
        unittest.main()

