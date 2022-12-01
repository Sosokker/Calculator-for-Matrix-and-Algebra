from parser.parser import polynomial_parse

class Polynomial:
    def __init__(self, poly):
        self.coeff = polynomial_parse(poly)
        self.degree = len(polynomial_parse(poly)) - 1