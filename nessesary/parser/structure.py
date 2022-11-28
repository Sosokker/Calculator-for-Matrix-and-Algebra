#VARIABLE AND NUMBER
VAR = 0
NUM = 1
POINT = 2

# OPERATOR
PLUS_S = 3
MINUS_S = 4
MUL_S = 5
DIV_S = 6
EXP_S = 7

# BRACKET AND PARENTHESES
LEFT_BRAC = 11
RIGHT_BRAC = 12
LEFT_PAR = 10
RIGHT_PAR = 11

#FUNCTION
SQRT_FUNC = 100
SIN_FUNC = 101
COS_FUNC = 102
TAN_FUNC = 103
SEC_FUNC = 104
COSEC_FUNC = 105
COT_FUNC = 106
ASIN_FUNC = 107
ACOS_FUNC = 108
ATAN_FUNC = 109
ASEC_FUNC = 110
ACOSEC_FUNC = 111
ACOT_FUNC = 112
FACTORIAL = 113
LOG = 114
LN = 115

ALPHABET_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 
                    'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's'
                    , 't', 'u', 'v', 'w', 'x', 'y', 'z']

NUM_LIST = ['1','2','3','4','5','6','7','8','9','0']

def general_parse(expr):

    result_list = []
    for value in expr:
        if value == "+":
            result_list.append(PLUS_S)
        elif value == "-":
            result_list.append(MINUS_S)
        elif value == "*":
            result_list.append(MUL_S)
        elif value == "/":
            result_list.append(DIV_S)
        elif (value == "^") or (value == "*"):
            result_list.append(EXP_S)
        elif value == ".":
            result_list.append(POINT)

        elif value == "(":
            result_list.append(LEFT_PAR)
        elif value == ")":
            result_list.append(RIGHT_PAR)
        elif value == "[":
            result_list.append(LEFT_BRAC)
        elif value == "]":
            result_list.append(RIGHT_BRAC)

        elif value in ALPHABET_LIST:
            result_list.append(VAR)
        elif value in NUM_LIST:
            result_list.append(NUM)

    """
    MEANING OF EACH PATTERN EXPRESSION.
        RESULT_LIST     MEANING
        [1,1,1,...]       1231..
        [0,0,0]            xyz
        [1,1,2,1,1]       12.32
        [1,1,0]            15x
        [10,11]            ()
        [12,13]            []
        [114,10,,11]      log()
        [115,10,,11]       ln()
        [1,1,113]          31!
        [101,10,,11]      sin()
    [1,0,3,10,1,2,1,
  101,10,1,1,1,11,11]   5x+(4.2sin(324))
     """

