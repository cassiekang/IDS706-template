"""
Test goes here

"""

from main import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(3, -5), -2)

if __name__ == '__main__':
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    print("All tests passed.")
