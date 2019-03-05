import unittest
from app.src.app import add_numbers


class MyTest(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 1), 2)
        self.assertEqual(add_numbers(1, -1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(1.0, 1), 2)
        self.assertEqual(add_numbers(1.1, 1.1), 2.2)
        self.assertEqual(add_numbers(40, 2), 42)
        self.assertEqual(add_numbers(42, 2), 44)


if __name__ == '__main__':
    unittest.main()
