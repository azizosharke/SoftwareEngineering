from functions import *
import unittest


class convert_rpn_test(unittest.TestCase):
    # tests a bunch of expression inputs to see if it correctly outputs an RPN list.
    def test_convert_rpn(self):
        test_dict = { "1 + 1"         : [1,1,'+'],
                      "3 + 4 * 5"     : [3,4,5,'*','+'],
                      "(3+4)*(5 - 2)" : [3,4,'+',5,2,'-','*'],
                      "(1+2.5)^(6/3)" : [1,2.5,'+',6,3,'/','^'],
                      "1+102/17+4"    : [1,102,17,'/','+',4,'+']
                    }
        for expression in test_dict:
            self.assertEqual(convert_rpn(expression), test_dict[expression])
            
class solve(unittest.TestCase):
    # tests a bunch of tuple inputs in RPN form to see if it correctly outputs a number.
    def test_solve_rpn(self):
        test_dict = { (1,1,'+')                : 2,
                      (3,4,5,'*','+')          : 23,
                      (3,4,'+',5,2,'-','*')    : 21,
                      (1,2.5,'+',6,3,'/','^')  : 12.25,
                      (1,102,17,'/','+',4,'+') : 11
                    }
        for tuple in test_dict:
            self.assertEqual(solve_rpn(list(tuple)), test_dict[tuple])
            
class calc(unittest.TestCase):
    # tests a bunch of expression inputs to see if it correctly outputs a number.
    def test_calculator(self):
        test_dict = { "1 + 1"         : 2,
                      "3 + 4 * 5"     : 23,
                      "(3+4)*(5 - 2)" : 21,
                      "(1+2.5)^(6/3)" : 12.25,
                      "1+102/17+4"    : 11
                    }
        for expression in test_dict:
            self.assertEqual(calculator(expression), test_dict[expression])
            
class convert_exp_test(unittest.TestCase):
    # tests a bunch of expression inputs to see if it correctly outputs an expression list.
    def test_convert_exp_to_list(self):
        test_dict = { "1 + 1"         : [1,'+',1],
                      "3 + 4 * 5"     : [3,'+',4,'*',5],
                      "(3+4)*(5 - 2)" : ['(',3,'+',4,')','*','(',5,'-',2,')'],
                      "(1+2.5)^(6/3)" : ['(',1,'+',2.5,')','^','(',6,'/',3,')'],
                      "1+102/17+4"    : [1,'+',102,'/',17,'+',4]
                    }
        for expression in test_dict:
            self.assertEqual(convert_exp_to_list(expression), test_dict[expression])

class number(unittest.TestCase):
    # test one checks if it returns true or false depending on input
    def test_one(self):
        testcase = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
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
        num1 = 3
        operator = "+"
        num2 = 7
        expected = 10
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_negative_number(self):
        num1 = -3
        operator = "+"
        num2 = 7
        msg = "enter a positive integer"
        expected = 10
        self.assertNotEqual(operation(num1, operator, num2), expected, msg)

    def test_multiply(self):
        num1 = 3
        operator = "*"
        num2 = 7
        expected = 21
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_subtract(self):
        num1 = 3
        operator = "-"
        num2 = 7
        expected = -4
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_divide(self):
        num1 = 3
        operator = "/"
        num2 = 7
        expected = 0.42857142857142855
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_power_of_num(self):
        num1 = 7
        operator = "^"
        num2 = 2
        expected = 49
        self.assertEqual(operation(num1, operator, num2), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)