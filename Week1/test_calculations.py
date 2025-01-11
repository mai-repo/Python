# Create a separate file for your unit tests (e.g., test_calculations.py). In this file, import the functions you defined and write unit tests for each function. Here's an example structure:

#unit test is a built in module for writing and running tests
import unittest
from Week1.main import subtract_numbers, divide_numbers

class TestCalculations(unittest.TestCase):
        def test_subtract_numbers(self):
                self.assertEqual(subtract_numbers(5, 3), 2)
                self.assertEqual(subtract_numbers(1, 1), 0)
        
        def test_divide_numbers(self):
                self.assertEqual(divide_numbers(10, 0), "Cannot divide by 0")
                self.assertEqual(divide_numbers(20, 2), 10)

        # """This is a failed test """
        # def test_add_numbers(self):
        #         self.assertEqual(add_numbers(5, 3), 8)
        #         self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == '__main__':
        unittest.main()

