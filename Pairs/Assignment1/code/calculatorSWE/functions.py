from sys import exit

precedence = {')': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


# Function to check if a given character is a number.
# returns true/false.

def is_number(token):
    return str(token).replace('.', '').isdigit()


# Function to check if a given character is an operator.
# returns true/false.

def is_operator(token):
    return token in ['+', '-', '*', '/', '^', '(', ')']


# Function to solve a given mathematical equation, provided as a string.
# Supports parentheses, +, -, *, /, ^, and floating point numbers.
# E.G. { calculator("3.5 ^ 2")       => 12.25
#        calculator("(4/2) * (3-1)") => 4.00   }

def calculator(expression):
    # Divide up the expression into a list of its constituent parts.
    exp_list = convert_exp_to_list(expression)

    # Check for invalid tokens in that list.
    for token in exp_list:
        if (not is_number(token)) and (not is_operator(token)):
            print('Invalid token: ' + token)
            exit()

    return solve_rpn(convert_rpn(expression))  # Convert the expression to RPN, then solve it.


# Function that converts a string containing a standard mathematical expression
# into a list containing an expression written in Reverse Polish Notation.
# Uses the shunting yard algorithm.
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm#Graphical_illustration
# Not going to try to explain the algorithm using comments. Check out the above webpage!


def convert_rpn(expression):
    exp_list = convert_exp_to_list(expression)
    output = []
    stack = []
    for token in exp_list:
        if is_number(token):
            output.append(token)
        else:
            if token == '(':
                stack.insert(0, token)
            elif token == ')' and stack:
                while stack[0] != '(' and stack:
                    output.append(stack[0])
                    del stack[0]
                if (not stack) or stack[0] != '(':
                    print("Invalid formatting of parentheses in expression.")
                    exit()
                del stack[0]
            else:
                if stack:
                    while (stack and
                           (token != '^' and precedence.get(token) <= precedence.get(stack[0])) or
                           (token == '^' and precedence.get(token) < precedence.get(stack[0]))):
                        output.append(stack[0])
                        del stack[0]
                stack.insert(0, token)
    while stack:
        output.append(stack[0])
        del stack[0]
    return output


# Function to solve RPN. Takes a list in RPN form and outputs a floating point number.

def solve_rpn(input_list):
    stack = []

    for token in input_list:                     # For each character in the RPN string...
        if is_number(token):                     # If it's a number...
            stack.append(token)                  # | If it's a number, put it on the stack.
        else:                                    # If it's an operator...
            try:                                 # |
                y = stack.pop()                  # | Take the last two numbers from the stack
                x = stack.pop()                  # | and apply the operation to them,
            except IndexError:                   # | (If it doesn't work that means that
                print("Invalid expression.")     # |  the expression is wrong somehow
                exit()                           # |
            stack.append(operation(x, token, y)) # | then put the result on the stack.
    return stack.pop()                           # The result is the last number on the stack.


# Function to convert a string expression (i.e. "2.3 + 1*4") into
# a list containing each section of the expression (i.e. [2.3,'+',1,'*',4])

def convert_exp_to_list(input_string):
    output_list = []
    n = 0
    while n != len(input_string):               # For each character in the string...
        if is_number(input_string[n]):          # If it's a number...
            temp = input_string[n]              # |
            while True:                         # |
                if n + 1 >= len(input_string):  # | And it's the last number...
                    temp = float(temp)          # | | Convert it to a float.
                    output_list.append(temp)    # | | Append the number to the list.
                    break                       # |
                elif (is_number(input_string[n + 1]) or
                     (input_string[             # |
                           n + 1] == '.')):     # | If the next char after this number is a number, or if it's a dec point...
                    temp += input_string[n + 1] # | | Combine it with any numbers or decimal points that came before it.
                    n += 1                      # | | Go back to the top of the loop.
                    continue                    # |
                temp = float(temp)              # | If the char after this number isn't a number...
                output_list.append(temp)        # | Add all of the numbers we've put together to the list.
                break                           # |
        elif input_string[n] != ' ':            # Otherwise, if it's not a number...
            output_list.append(input_string[n]) # | Add it to the list. Ignore whitespace.
        n += 1
    return output_list


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
            print("Try using limits next time you sussy baka\nDIVISION BY 0 ERROR.")
            exit()
    elif operator == "^":
        return num1 ** num2


