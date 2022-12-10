def add_neg_sign(expr: str, is_neg: bool) -> str:
    """
    Add negative sign to expression if 
    is_neg is True.
    """
    if is_neg:
        expr = "-" + expr
    return expr

def add_exp_sign(expr):
    return expr.replace("^", "**")

def is_neg(expr, i) -> bool:
    """
    Check if input expression is negative or not.
    """
    n = len(expr)
    neg_sign = 0
    while i < n and expr[i] == "-":
        neg_sign += 1
        i += 1
    i -= 1
    return neg_sign%2 != 0

def is_num(char: str) -> bool:
    """
    Check if char agrument is number or not.
    """
    return char in ['1','2','3','4','5','6','7','8','9','0']

def is_op(char: str) -> bool:
    """
    Check if char agrument is operator or not.
    """
    if char in ["+","-","*","/","^","("]:
        return True
    return False

def is_letter(char: str) -> bool:
    """
    Check if char agrument is string character or not.
    """
    return "a" <= char <= "z"

def is_func(expr: str, i: int, result: str) -> tuple[bool, str, int]:
    """
    Check if expression is a function or not.
    """
    result = ""
    while i < len(expr):
        if not is_letter(expr[i]):
            i -= 1
            break
        result += expr[i]
        i += 1
    new_index = i
    return len(result) > 1, result, new_index

def priority(char: str) -> int:
    """
    set precedence for each operator.
    This program use PEMDAS RULE as main rule 
    to implement.
    """
    if char == "+" or char == "-":
        return 2
    elif char == "*" or char == "/":
        return 3
    elif char == "^":
        return 4
    return 5

def parsing_num(expr: str, i: int):
    """
    Find the first number after the index i.
    Return string of number and the end index of it.

    >>> parsing_num("123+456", 0)
    ("123",2)
    """
    n = len(expr)
    start = i

    while (i < n) and (is_num(expr[i]) or expr[i] == "."):
        i += 1
    return expr[start:i], i - 1

def make_postfix(expr: str):
    """
    Change infix notation intoPostfix Notation
    Postfix Notation has a better ability to 
    set priority of each operand.
    
    >>> make_postfix(" 3*4 + 2*5")
    3 4 * 2 5 * +

    >>> make_postfix("(2-3+4)*(5+6*7)")
    2 3 - 4 + 5 6 7 * + *
    """


    if len(expr) == 0:
        return ""

    op_stack = []
    result = ""
    temp = ""
    neg = False
    has_func = False
    i = 0
    while i < len(expr):
        char = expr[i]
        func_check, temp, last_index = is_func(expr, i, temp)
        if char == " " or char == "," or char == ":":
            i += 1
            continue

        if is_num(char):
            num, i = parsing_num(expr, i)
            result += add_neg_sign(num, neg)
            neg = False
            result += " "
            i += 1
            

        elif char == ")":
            found = False
            while len(op_stack) != 0:
                top = op_stack.pop()
                if top == "(":
                    found = True
                    break
                else:
                    result += top
                    result += " "
            i += 1
            if not found:
                raise ValueError("Parentheses Error!")

        elif is_op(char) or func_check:
            isfunc = len(temp) > 1
            if (not isfunc) and (char == "-"):
                if i == 0 or is_op(expr[i-1]):
                    neg = is_neg(expr, i)
                    i += 1
                    continue

            while len(op_stack) != 0:
                top = op_stack[-1]
                priority1 = (priority(top) < priority(char))
                priority2 = (priority(top) == priority(char))
                if char == "(" or top == "(" or priority1 or (priority2 and char == "^"):
                     break
                result += top
                op_stack.pop()
                result += " "

            if isfunc:
                op_stack.append(add_neg_sign(temp, neg))
                neg = False
                temp = ""
                i = last_index
                has_func = True
            else:
                op_stack.append(char)
            i += 1

        elif is_letter(char):

            result += add_neg_sign(char, neg)
            neg = False
            result += " "
            i += 1

        else:
            raise ValueError("Can't Parse this Letter!")
        
    while len(op_stack) != 0:
        top = op_stack.pop()
        result += top
        result += " "
    i += 1
    return result[:len(result)-1], has_func

def insert_mul_sign(expr):
    """
    Insert multiplication sign to expression(*)
    >>> insert_mul_sign("xx")
    x*x
    >>> insert_mul_sign("xy+xsin(xy)+12x+y")
    x*y+x*sin(x*y)+12*x+y
    >>> insert_mul_sign("(12x)(1+(12y+sin(x^3-2))(x+2))")
    (12x)*(1+(12*y+sin(x^3-2))*(x+2))
    """
    function_list = [
                    "sin","cos","tan", "cosec", "sec", "cot",
                    "arcsin","arccos","arctan", "arcsec", 
                    "arccosec", "arccot"
                    ]
    i = 0
    result = ""
    f_name = ""
    neg = False
    new = ""
    for ind in range(len(expr)):
        if expr[ind] == " ":
            continue
        new += expr[ind]
    expr = new

    while i < len(expr):
        char = expr[i]
        check_func, f_name, last_index = is_func(expr, i, f_name)
        if is_num(char):
            num, i = parsing_num(expr, i)
            result += add_neg_sign(num, neg)
            neg = False
            i += 1
            if expr[-1] != char:
                if expr[i] != ")" and not is_op(expr[i]):
                    result += "*"
                elif expr[i] == "(":
                    result += "*"
        elif char == ")":
            try:
                if expr[i+1] != ")" and is_op(expr[i+1]):
                    result += ")*"
            except IndexError:
                result += char
            i += 1

        elif is_op(char):
            result += char
            i += 1

        elif check_func:
            for f_check in function_list:
                if f_check in f_name:
                    real_func_name = f_check

            check_list = [1 for n in function_list if n in f_name]
            if sum(check_list) > 0:
                result += f_name.replace(real_func_name, "*")
                result += real_func_name
                i = last_index + 1
            else:
                count = len(f_name)
                for ind in range(len(f_name)+1):
                    if ind % 2 != 0:
                        f_name = f_name[:ind] + "*" + f_name[ind:]
                result += f_name
                i = last_index + count

        elif is_letter(char) or char == "(":
            if result[-1] != "*":
                if (result[i] != "(") and (char != "("):
                    result += "*"
            result += char
            # if not is_op(expr[i]):
            #     result += "*"
            i += 1

    return result

import re

def parse_poly(expr: str) -> list:
    """
    Parse string of basic polynomial expression.
    Note: Only Specific form of polynomial that
    this function can parse.
    """
    pattern = re.compile('([-+]?\s*\d*\.?\d*)(x?\^?\d?)')
    expo_pattern = re.compile('x\^?(\d)?')
    coeff_var_list = pattern.findall(expr)
    store = {}
    highest_expo = 0
    for coeff, var in coeff_var_list:
        if not coeff: 
            coeff = 0
        elif coeff == '-': 
            coeff = -1
        elif coeff == '+': 
            coeff = 1
        try:
            coeff = eval(coeff)
        except:
            pass

        expo = expo_pattern.findall(var)
        if len(expo) == 0:
            expo = 0
        elif '' in expo:
            expo = 1
        else:
            expo = expo[0]
        try:
            expo = eval(expo)
        except:
            pass
        
        if expo >= highest_expo:
            highest_expo = expo

        temp = [coeff, expo]
        if var not in store:
            store[var] = temp
        else:
            store[var][0] += temp[0]
    print(store)
    result = [0 for i in range(highest_expo+1)]
    for item in store.values():
        coeff = item[0]
        expo = item[1]
        result[expo] = coeff
    return result

# print(parse_poly("-x^2+2x"))
# print(make_postfix("(2-3+4)*(5+6*7)"))
# print(make_postfix("12sin(x^2)+(4x+12*3)-5"))
# print(insert_mul_sign("12x"))
# print(insert_mul_sign("5x+12y+421abcde+1"))
# print(insert_mul_sign("12((x+12x)x)"))
# print(insert_mul_sign("xsin(x^2)"))
# print(insert_mul_sign("xy+xsin(xy)+12x+y"))
# print(insert_mul_sign("5(1+2*3^12)(12-5(4^2)) + (1-3*4)12"))
# print(insert_mul_sign("(1+2)(3+4)"))
# print(add_exp_sign("x^2^3"))
# print(parse_poly("x^4+1+12x^3-3x^2+5"))