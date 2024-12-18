# Create a separate file for your unit tests (e.g., test_calculations.py). In this file, import the functions you defined and write unit tests for each function. Here's an example structure:
      
import unittest
from First_Assignment import add_numbers, multiply_numbers

class TestCalculations(unittest.TestCase):
        def test_add_numbers(self):
                self.assertEqual(add_numbers(5, 3), 8)
                self.assertEqual(add_numbers(-1, 1), 0)

        def test_multiply_numbers(self):
                self.assertEqual(multiply_numbers(4, 5), 20)
                self.assertEqual(multiply_numbers(-2, 3), -6)

if __name__ == '__main__':
        unittest.main()

