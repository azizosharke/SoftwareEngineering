from utility import is_number, is_operator


# Function to convert a string expression into a list
def convert_to_list(input_to_calc: str):
    last_num = False
    # if true, next operator will be applied to number (for negation)
    next_unary = True
    negate = False
    floating = 0    # if number floating (ie not 0), divide char by 10^floating and add to last index
    expr = []
    for i, char in enumerate(input_to_calc):

        if is_number(char):
            if floating != 0:
                if char == ".":
                    return "Error: number contains two decimal points"
                if negate:
                    # convert string to number, subtract from end of number in list
                    expr[-1] = expr[-1] - ((ord(char) - 48) / 10 ** floating)
                else:
                    # convert string to number, add onto end of number in list
                    expr[-1] = expr[-1] + ((ord(char) - 48) / 10 ** floating)
                floating += 1

            elif last_num:
                if negate:
                    # convert string to number, subtract from end of number in list
                    expr[-1] = expr[-1] * 10 - (ord(char) - 48)
                else:
                    # convert string to number, add onto end of number in list
                    expr[-1] = expr[-1] * 10 + (ord(char) - 48)

            else:
                last_num = True
                if negate:
                    expr.append((ord(char) - 48) * -1)
                else:
                    # convert from string to number and add to list
                    expr.append(ord(char) - 48)

            # if operator follows number, it is not unary
            next_unary = False

        elif char == " ":
            last_num = False
            floating = False

        elif char == "-" and next_unary:
            try:
                next_bracket = False
                for j in range(1, len(input_to_calc) - i):
                    if input_to_calc[i+j] == '(':
                        next_bracket = True
                        break
                    elif input_to_calc[i+j] != ' ':
                        break
                if not negate and next_bracket:
                    expr.append('¬')
                else:
                    negate = not negate
            except IndexError:
                return "Error: ends in -"
            floating = 0

        elif char == ")":
            expr.append(char)
            last_num = False
            negate = False
            floating = 0

        elif char == '.':
            if last_num == "":
                return "Error: must be a number before decimal point"
            if floating != 0:
                return "Error: number contains two decimal points"
            floating += 1

        elif is_operator(char) or char == '(':
            expr.append(char)
            last_num = False
            negate = False
            next_unary = True
            floating = 0

        else:
            if char == 'e' or char == 'l':
                expr.append(char)
            elif char == 'x' and expr[-1] == 'e':
                expr[-1] = char
            elif char == 'p' and expr[-1] == 'x':
                expr[-1] = char
            elif char == 'o' and expr[-1] == 'l':
                expr[-1] = char
            elif char == 'g' and expr[-1] == 'o':
                expr[-1] = char
            else:
                return "Error: unrecognised character: " + str(char)

            last_num = False
            negate = False
            next_unary = False
            floating = 0
    # print(expr)         # uncomment to see expression
    return expr


def validate_expression(expression):
    if is_operator(expression[0]):
        return "Error: starts with operator"
    if is_operator(expression[-1]):
        return "Error: ends with operator"

    last_op = ' '
    last_num = ''
    last_bracket = ''
    last_unary = False
    brackets = 0
    for i in expression:
        if type(i) == int or type(i) == float:
            if last_num != '':
                return "Error: two numbers in a row: " + last_num + " and " + str(i)
            if last_bracket == ')':
                return "Error: operator needed after right bracket"
            last_op = ''
            last_num = str(i)
            last_bracket = ''
            last_unary = False

        elif is_operator(i):
            if last_op != '':
                return "Error: two operators in a row: " + last_op + " and " + i
            if last_bracket == '(':
                return "Error: operator after left bracket"
            last_op = i
            last_num = ''
            last_bracket = ''
            last_unary = False

        elif i == "(":
            if last_op == "" and not last_unary:
                return "Error: operator needed before left bracket"
            brackets += 1
            last_op = ''
            last_num = ''
            last_bracket = "("
            last_unary = False

        elif i == ')':
            if last_op != '':
                return "Error: operator before right bracket"
            brackets -= 1
            last_op = ''
            last_num = ''
            last_bracket = ')'
            last_unary = False

        elif i == 'p' or i == 'g':
            last_unary = True

    if brackets > 0:
        return "Error: open left bracket"
    if brackets < 0:
        return "Error: open right bracket"
    return None