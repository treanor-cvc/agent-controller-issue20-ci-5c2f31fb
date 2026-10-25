import unittest

from feature_a import add


class AddBehaviorTests(unittest.TestCase):
    def test_signed_integer_addition(self):
        cases = [
            (2, 3, 5),
            (-2, -3, -5),
            (-7, 3, -4),
            (7, -3, 4),
            (-8, 8, 0),
            (0, 0, 0),
            (0, 9, 9),
            (9, 0, 9),
            (0, -9, -9),
            (-9, 0, -9),
        ]
        for left, right, expected in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(add(left, right), expected)

    def test_arbitrary_precision_integers(self):
        huge = 10 ** 100
        self.assertEqual(add(huge, huge), 2 * huge)
        self.assertEqual(add(-huge, -huge), -2 * huge)
        self.assertEqual(add(huge, -huge + 1), 1)


if __name__ == "__main__":
    unittest.main()
