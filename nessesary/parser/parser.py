def add_neg_sign(expr: str, is_neg: bool) -> str:
    """
    Add negative sign to expression if 
    is_neg is True.
    """
    if is_neg:
        expr = "-" + expr
    return expr

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

def is_func(expr: str, i: int, result: str) -> bool:
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
    return result[:len(result)-1]
