from parser.parser import parse_poly

class Polynomial:
    def __init__(self, poly):
        if isinstance(poly, str):
            self.coeff = parse_poly(poly)
            self.degree = len(parse_poly(poly)) - 1
            self.string_form = poly
        elif isinstance(poly, list):
            self.coeff = poly
            self.degree = len(poly) - 1
            self.string_form = self.to_str()
        else:
            raise ValueError

    #[degree0, degree1, degree2]
    def __add__(self, other):
        """
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p2 = Polynomial([1, 1, 1, 1, 1])
        >>> p3 = p1 + p2
        >>> p3
        2x^4+2x^3+2x^2+2x+2
        """
        if isinstance(other, Polynomial):
            for degree_index in range(self.degree):
                self.coeff[degree_index] += other.coeff[degree_index]
        if isinstance(other, int) or isinstance(other, float):
            pass


    def __sub__(self, other):
        """
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p2 = Polynomial([1, 1, 1, 1, 1])
        >>> p3 = p1 - p2
        >>> p3
        0
        """
        if isinstance(other, Polynomial):
            for degree_index in range(self.degree):
                self.coeff[degree_index] -= other.coeff[degree_index]
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0 for i in self.degree + other.degree]
            for self_index in range(self.degree):
                for other_index in range(other.degree):
                    result[self_index+other_index] += self.coeff[self_index]*other.coeff[other_index]

    def __pow__(self):
        pass

    def __truediv__(self):
        pass

    def to_str(self):
        """
        convert coefficient list into string.
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p1.to_str()
        x^4+x^3+x^2+x+1
        >>> p2 = Polynomial([-2, 4, 0, -1, 2])
        >>> p2.to_str()
        2x^4-x^3+4x-2
        """
        result = []
        for ind in range(len(self.coeff)):
            if self.coeff[ind]:
                if ind == 0:
                    temp = ""
                elif ind == 1:
                    temp = "x"
                else:
                    temp = "x^"+str(ind)
                result.append(str(self.coeff[ind])+temp)

        if result:
            result.reverse()
            return " + ".join(result)
        else:
            return "0"

    def __str__(self) -> str:
        return self.string_form