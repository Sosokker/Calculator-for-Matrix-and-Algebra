from nessesary.parser.parser import parse_poly
from nessesary.fraction import to_fraction

class Polynomial:
    def __init__(self, poly, fracmode=False):
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
        self.fracmode = fracmode
        if fracmode:
            for c_index in range(len(self.coeff)):
                try:
                    self.coeff[c_index] = to_fraction(self.coeff[c_index])
                except:
                    raise ValueError("Can't turn all number into fraction.")

    #[degree0, degree1, degree2]
    def __add__(self, other):
        """
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p2 = Polynomial([1, 1, 1, 1, 1])
        >>> p3 = p1 + p2
        >>> str(p3)
        '2x^4+2x^3+2x^2+2x+2'
        """
        if isinstance(other, Polynomial):
            large_index = max([self.degree, other.degree])
            temp = [0 for i in range(large_index)]
            result = Polynomial(temp)
            for degree_index in range(self.degree):
                result.coeff[degree_index] = self.coeff[degree_index] + other.coeff[degree_index]
            return result
        elif isinstance(other, (int, float)):
            result = Polynomial(self.coeff)
            result.coeff[0] += other
            return result

    def __sub__(self, other):
        """
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p2 = Polynomial([1, 1, 1, 1, 1])
        >>> p3 = p1 - p2
        >>> str(p3)
        '0'
        """
        if isinstance(other, Polynomial):
            large_index = max([self.degree, other.degree])
            temp = [0 for i in range(large_index)]
            result = Polynomial(temp)
            for degree_index in range(self.degree):
                result.coeff[degree_index] = self.coeff[degree_index] - other.coeff[degree_index]
            return result
        elif isinstance(other, (int, float)):
            result = Polynomial(self.coeff)
            result.coeff[0] -= other
            return result

    def __mul__(self, other):
        """
        >>> p1 = Polynomial([1, 1])
        >>> p2 = Polynomial([1, 1])
        >>> p3 = p1 * p2
        >>> str(p3)
        x^2+2x+1
        """
        if isinstance(other, Polynomial):
            result = [0 for i in self.degree + other.degree]
            for self_index in range(self.degree):
                for other_index in range(other.degree):
                    result[self_index+other_index] += self.coeff[self_index]*other.coeff[other_index]
            poly_result = Polynomial(result)
            return poly_result
        elif isinstance(other, int) or isinstance(other, float):
            result = [0 for i in self.degree + other.degree]
            for self_index in range(self.degree):
                result[self_index+other_index] += self.coeff[self_index]*other
            poly_result = Polynomial(result)
            return poly_result

    def __pow__(self, other):
        """
        >>> p1 = Polynomial([1, 1])
        >>> str(p1 ** 2)
        x^2+2x+1
        """
        result = Polynomial([0])
        if isinstance(other, int) and other >= 0:
            if other == 0:
                return Polynomial([1])
            else:
                for i in range(other):
                    result += self * self
                return result

    def __truediv__(self):
        pass

    def to_str(self) -> str:
        """
        convert coefficient list into string.
        >>> p1 = Polynomial([1, 1, 1, 1, 1])
        >>> p1.to_str()
        'x^4+x^3+x^2+x+1'
        >>> p2 = Polynomial([-2, 4, 0, -1, 2])
        >>> p2.to_str()
        '2x^4-x^3+4x-2'
        """
        # result = []
        # for ind in range(len(self.coeff)):
        #     if self.coeff[ind]:
        #         if ind == 0:
        #             temp = ""
        #         elif ind == 1:
        #             temp = "x"
        #         else:
        #             temp = "x^"+str(ind)
        #         result.append(str(self.coeff[ind])+temp)

        # if result:
        #     result.reverse()
        #     return "+".join(result)
        # else:
        #     return "0"

        result = []
        i = len(self.coeff) - 1
        while i >= 0:
            if self.coeff[i] != 0:
                if self.coeff[i] < 0:
                    result.append("-")

                elif len(self.coeff) != 0:
                    result.append("+")

            elif self.coeff[i] == 0:
                i -= 1
                continue

            if self.coeff[i] != 1 and self.coeff[i] != -1:
                result.append(str(abs(self.coeff[i])))

            if (i == len(self.coeff) - 1):
                result.append(str(self.coeff[i]))

            if (self.coeff[i] == 1) and (i != len(self.coeff) - 1):
                result.append(str(1))

            if i == 1:
                result.append("x")

            if i > 1:
                result.append("x^"+str(i))
            i -= 1

        if result[0] == "+" or result[0] == "-":
            del result[0]
        result = "".join(result)

        return result

    def solve(self) -> tuple:
        degree = len(self.coeff) - 1
        if degree == 2:
            a, b, c = self.coeff[2], self.coeff[1], self.coeff[0]
            if a == 0:
                if b == 0:
                    if c == 0:
                        return (0, None)
                    else:
                        return (c, None)
                else:
                    return (-c/b, None)
            else:
                root_term = b**2-4*a*c
                if root_term < 0:
                    res1 = f"({-b}+{to_imag(root_term**0.5)})/{2*a}"
                    res2 = f"({-b}-{to_imag(root_term**0.5)})/{2*a}"
                    return (res1, res2)
                else:
                    if root_term == 0:
                        return (-b/(2*a), None)
                    else:
                        try:
                            res1 = (-b-(root_term)**0.5)/(2*a)
                            res2 = (-b+(root_term)**0.5)/(2*a)
                        except TypeError:
                            res1 = (-b-(root_term)**0.5)/(2*a)
                            res2 = (-b+(root_term)**0.5)/(2*a)                
                        return (res1, res2)

    def __str__(self) -> str:
        return self.string_form

def to_imag(num) -> str:
    """
    >>> to_imag(-10)
    '10i'
    >>> to_imag(-10.12)
    '10.12i'
    """
    num = abs(num)
    return f"{num}i"

# p1 = Polynomial("x^2+2x+1", fracmode=True)
# p2 = Polynomial("x^2+2x+1", fracmode=False)

# print(p1.solve())

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)