from evaluation import *
from functions import *
from utility import *
import unittest


class Number(unittest.TestCase):

    def test_one(self):
        testcase = "eydfhsjdfhsjdfhjsdhfjshdfjsdfsdf9"
        expected = [True, False]
        self.assertIn(is_number(testcase), expected)

    def test_without_input(self):
        testcase = " ",
        self.assertFalse(is_number(testcase))


class Operator(unittest.TestCase):
    def test_positive_input(self):
        testcase = "+"
        expected = True
        self.assertEqual(is_operator(testcase), expected)

    def test_empty_input(self):
        testcase = " "
        expected = False
        self.assertEqual(is_operator(testcase), expected)


class Operations(unittest.TestCase):
    def test_add(self):
        num1 = 4
        operator = "+"
        num2 = 7
        expected = 11
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_negative_number(self):
        num1 = -4
        operator = "+"
        num2 = 7
        msg = "enter a positive integer"
        expected = 11
        self.assertNotEqual(operation(num1, operator, num2), expected, msg)

    def test_multiply(self):
        num1 = 4
        operator = "*"
        num2 = 5
        expected = 20
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_subtract(self):
        num1 = 2
        operator = "-"
        num2 = 5
        expected = -3
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_divide(self):
        num1 = 3
        operator = "/"
        num2 = 7
        expected = 0.42857142857142855
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_power_of_num(self):
        num1 = 9
        operator = "^"
        num2 = 2
        expected = 81
        self.assertEqual(operation(num1, operator, num2), expected)


class Equation(unittest.TestCase):

    def test_calculator(self):
        test_dict = {"2 + 2": 4,
                     "6 + 7 * 8": 62,
                     "(7+8)*(6 - 4)": 30,
                     "(1+2.5)^(6/3)": 12.25,
                     "1+102/17+4": 11,
                     "4.45 * -(45 + log(3 + exp(2)) / 5)": -202.333,
                     "5/(3-3)": "Error: division by zero"
                     }
        for expression in test_dict:
            self.assertEqual(calculator(expression), test_dict[expression])

    def test_convert_to_list(self):
        test_dict = {"2 + 2": [2, '+', 2],
                     "5 + 6 * 7": [5, '+', 6, '*', 7],
                     "(7+8)*(6 - 4)": ['(', 7, '+', 8, ')', '*', '(', 6, '-', 4, ')'],
                     "(6+3.3)^(8/2)": ['(', 6, '+', 3.3, ')', '^', '(', 8, '/', 2, ')'],
                     "2+191/21+8": [2, '+', 191, '/', 21, '+', 8],
                     "4 * -(5+3)": [4, '*', '¬', '(', 5, '+', 3, ')'],
                     "4 * --(5+3)": [4, '*', '(', 5, '+', 3, ')'],
                     "3+1.2.3": "Error: number contains two decimal points"
                     }
        for expression in test_dict:
            self.assertEqual(convert_to_list(expression), test_dict[expression])

    def test_validate_expression(self):
        to_test = [['(', 6, '+', 3.3, ')', '^', '(', 8, '/', 2, ')'],
                   [2, '+', '/', 21],
                   ['(', 6, '+', 3.3],
                   ['(', 6, '+', ')'],
                   ['/', '(', 3, '-', 1, ')']]

        expected = [None,
                    "Error: two operators in a row: + and /",
                    "Error: open left bracket",
                    "Error: operator before right bracket",
                    "Error: starts with operator"]

        for i in range(len(to_test)):
            self.assertEqual(validate_expression(to_test[i]), expected[i])

    def test_handle_unary(self):
        to_test = [['g', '(', 3, ')'],
                   [13, '+', 'g', '(', 13, '+', '(', 3, '*', 23, ')', ')'],
                   ['g', '(', 'g', '(', 3, ')', ')'],
                   ['g', '(', 3, '+', 'g', '(', 3, ')', ')'],
                   ['p', '(', 3, ')'],
                   ['p', '(', 'p', '(', 2, ')', '-', 2, ')', '-', 5],
                   [3, '*', '¬', '(', 4, '+', 10, ')'],
                   [2, '*', '¬', '(', 10, '/', '¬', '(', 8, '-', 3, ')', ')']]

        expected = [[1.0986122886681098],
                    [13, '+', 4.406719247264253],
                    [0.0940478276166991],
                    [1.4106484502391472],
                    [20.085536923187668],
                    [218.99657686275216, '-', 5],
                    [3, '*', -14],
                    [2, '*', 2]]

        for i in range(len(to_test)):
            self.assertEqual(handle_unary(to_test[i]), expected[i])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
