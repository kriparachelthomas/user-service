# tests/test_example.py
import unittest

# Example function you might want to test
def add(a, b):
    return a + b

# Test case class that inherits from unittest.TestCase
class TestExample(unittest.TestCase):
    
    # Test method for the add function
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # Assert that 1 + 2 equals 3
        self.assertEqual(add(-1, 1), 0)  # Assert that -1 + 1 equals 0
        self.assertEqual(add(0, 0), 0)   # Assert that 0 + 0 equals 0

# If the script is being run directly, run the tests
if __name__ == "__main__":
    unittest.main()
