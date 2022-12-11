from nessesary.polynomial import Polynomial
from nessesary.parser.parser import is_letter, is_op

def change_side(equa:str):
    """
    Change all left side expression of = sign
    to right side.
    >>> change_side("x+2-x^2 = 32-x^3")
    'x+2-x^2-32+x^3=0'
    """
    temp = ''
    for i in equa:
        if i == " ":
            temp += ""
        else:
            temp += i
    
    equa = temp
            
    llist = equa.split("=")
    left_side, right_side = llist[0], llist[1]

    temp = ''
    if (right_side[0] != "-") or (right_side[0] != "+"):
        temp += '+'
    temp += right_side
    right_side = temp
    for i in right_side:
        if i == "+":
            left_side += "-"
        elif i == "-":
            left_side += "+"
        else:
            left_side += i
    return left_side

def simplify(expr:str):
    """
    Use to_str() method of polynomial.
    to sum and sub all coefficient.
    """
    poly = Polynomial(expr)
    try:
        result = poly.to_str()
        return result
    except:
        raise ValueError

def solver(expr:str):
    """
    Solve expression that using polynomial solve().
    """
    poly = Polynomial(expr)
    try:
        result = poly.solve()
        return result
    except:
        raise ValueError

def poly_expand(expr:str):
    """
    Add Polynomial Text to all element that
    can make polynomial.
    >>> poly_expand("(3x+2)^3+4x+5-2+(5x^2)^3")
    'Polynomial("3x+2")**3+Polynomial("4x")+Polynomial("5x^2")**3'
    """
    i = 0
    result = ""
    found = False
    added = False
    while i < len(expr):
        char = expr[i]
        if char == "(":
            result += "Polynomial("
            i += 1
            found = True
        else:
            if not found:
                if added and is_op(char):
                    result += f"){char}"

                    added = False
                if is_op(char) and char != "^":
                    result += f"{char}Polynomial("
                    i += 1
                    added = True
                    continue
            result += char
            i += 1

        if char == ")":
            found = False

    result = result.replace("++", "+").replace("--","-")
    result = result.replace("^^", "^")
    result = result.replace("))", ")")
    result = result.replace("^", "**")
    result = result.replace("Polynomial(Polynomial(", "Polynomial(")
    return result
