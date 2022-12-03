pre = {')': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


# Function to check if a given character is a number.
# returns true/false.
def is_number(token):
    return str(token).replace('.', '').replace('-', '').isdigit()


# Function to check if a given character is an operator.
# returns true/false.
def is_operator(token):
    return token in ['+', '-', '*', '/', '^']


# Function to check if a given character is a unary operator.
# returns true/false.
def is_unary(token):
    return token in ['p', 'g', '¬']     # p is exp, g is log, ¬ is negation


# Function to check the operation and division by 0 .
# returns the results .
def operation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: division by zero"
    elif operator == "^":
        return num1 ** num2


def get_precedence(token):
    if token == "+":

        return 1
    elif token == "-":
        return 1
    elif token == "*":
        return 2
    elif token == "/":
        return 2
    elif token == "^":
        return 3
    return -1
