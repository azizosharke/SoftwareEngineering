from functions import convert_to_list, validate_expression
from utility import get_precedence, operation, is_unary
from math import exp, log


# Function to solve a mathematical equation
# Supports (), +, -, *, /, ^, and floating point numbers.
def calculator(equation: object) -> object:
    list = convert_to_list(equation)
    if type(list) == str:
        return list

    validation_result = validate_expression(list)
    if validation_result is not None:
        return validation_result
    else:
        partial_result = handle_unary(list)
        if type(partial_result) == str:
            return partial_result

        result = evaluate(partial_result)
        if type(result) == str:
            return result
        elif type(result) == int or type(result) == float:
            return round(result, 3)
        return "Error: Complex Result"


def perform_operation(val_stack, op_stack):
    val2 = val_stack.pop()
    val1 = val_stack.pop()
    op = op_stack.pop()
    res = operation(val1, op, val2)
    if type(res) == str:
        return res
    val_stack.append(res)
    return None


def evaluate(expr):
    val_stack = []
    op_stack = []
    for token in expr:
        if type(token) == int or type(token) == float:
            val_stack.append(token)
        elif token == "(":
            op_stack.append(token)

        elif token == ")":
            while len(op_stack) != 0 and op_stack[-1] != "(":
                err = perform_operation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.pop()  # discard "("

        else:
            while len(op_stack) != 0 and op_stack[-1] != "(" and get_precedence(op_stack[-1]) >= get_precedence(token):
                err = perform_operation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.append(token)

    while len(op_stack) != 0:
        err = perform_operation(val_stack, op_stack)
        if err is not None:
            return err
    return val_stack.pop()


def handle_unary(list):
    partial_result = []
    i = 0
    while i < len(list):
        if is_unary(list[i]):
            unary = list[i]
            part = []
            i += 1
            if list[i] != '(':
                return "Error: brackets should follow log or exp"

            brackets = 1
            while brackets != 0:
                i += 1
                if i >= len(list):
                    return "Error: open left bracket"
                elif list[i] == '(':
                    brackets += 1
                elif list[i] == ')':
                    brackets -= 1
                if brackets != 0:
                    part.append(list[i])

            handled_part = handle_unary(part)  # recursive call to function to handle nested log/exp
            result = evaluate(handled_part)
            if unary == 'p':
                partial_result.append(exp(result))
            elif unary == 'g':
                partial_result.append(log(result))
            else:
                partial_result.append(result * -1)
        else:
            partial_result.append(list[i])
        i += 1

    return partial_result
