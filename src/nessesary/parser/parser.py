import re

def parse_poly(expr: str) -> list:
    """
    Parse string of basic polynomial expression.
    Note: Only Specific form of polynomial that
    this function can parse.
    """
    temp1 = ''
    for i in expr:
        if i == " ":
            temp1 += ""
        else:
            temp1 += i
    expr = temp1
    pattern = re.compile('([-+]?\s*\d*\.?\d*)(x?\^?\d?)')
    expo_pattern = re.compile('x\^?(\d)?')
    coeff_var_list = pattern.findall(expr)[0:-1]
    store = {}
    highest_expo = 0
    for coeff, var in coeff_var_list:
        if not coeff: 
            coeff = 1
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

    result = [0 for i in range(highest_expo+1)]
    for item in store.values():
        coeff = item[0]
        expo = item[1]
        result[expo] = coeff
    return result