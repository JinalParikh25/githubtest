import unittest
from math_quiz import get_random_int, get_random_math_operator, get_result


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_math_operator(self):
        # Test generated operator is in [+,-,*] container or not.
        for _ in range(1000):
            rand_operator = get_random_math_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_get_result(self):

            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 4, '-', '6 - 4', 2),
                (9, 9, '*', '9 * 9', 81)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = get_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer,expected_answer)


if __name__ == "__main__":
    unittest.main()
