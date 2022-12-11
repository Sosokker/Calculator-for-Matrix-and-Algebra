from nessesary.parser.parser import parse_poly
from nessesary.fraction import to_fraction
from math import acos, cos, pi

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

        while len(self.coeff) < 3:
            self.coeff.append(0)

        self.degree = len(self.coeff)

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

    def solve(self) -> dict:
        degree = len(self.coeff) - 1
        sol = [{"real":0, "imag":0}, {"real":0, "imag":0}]
        if degree == 2:
            a, b, c = self.coeff[2], self.coeff[1], self.coeff[0]
            if a == 0:
                if b == 0:
                    if c == 0:
                        return sol
                    else:
                        sol[0]["real"] = c
                        del sol[1]
                        return sol
                else:
                    sol[0]["real"] = -c/b
                    del sol[1]
                    return sol
            else:
                root_term = b**2-4*a*c
                if root_term < 0:
                    # res1 = f"({-b}+{to_imag(root_term**0.5)})/{2*a}"
                    # res2 = f"({-b}-{to_imag(root_term**0.5)})/{2*a}"
                    sol[0]["real"] = -b/(2*a)
                    sol[1]["real"] = -b/(2*a)
                    sol[0]["imag"] = (abs(root_term)**0.5)/2*a
                    sol[1]["imag"] = (-abs(root_term)**0.5)/2*a
                    return sol
                else:
                    if root_term == 0:
                        sol[0]["real"] = -b/(2*a)
                        del sol[1]
                        return sol
                    else:
                        sol[0]["real"] = (-b-(root_term)**0.5)/(2*a)
                        sol[1]["real"] = (-b+(root_term)**0.5)/(2*a)            
                        return sol
        
        elif degree == 3:
            a, b = self.coeff[3], self.coeff[2]
            c, d = self.coeff[1], self.coeff[0]

            b, c, d = b/a, c/a, d/a

            temp_q = 3.0*c-(b*b)/9.0
            temp_r = (-(27.0*d)+b*(9*c-2.0*(b * b)))/54.0
            first_term = b/3
            temp_check = (temp_q**3)+(temp_r**2)
            sol = [{"real":0, "imag":0},{"real":0, "imag":0},{"real":0, "imag":0}]

            if temp_check > 0:
                temp = 1/3
                i = temp_r + (temp_check**0.5)
                if i < 0:
                    i = -(-i**(temp))
                else:
                    i = i**temp
                j = temp_r - (temp_check)**0.5
                if j < 0:
                    j = -(-j**(temp))
                else:
                    j = j**temp

                sol[0]["real"] = -first_term + i + j
                sol[2]["real"] = -(first_term+((i+j)/2))
                sol[1]["real"] = (first_term+((i+j)/2))
                sol[1]["imag"] = (3**0.5) * (-i+j)/2
                sol[2]["imag"] = -sol[1]["imag"]

                return sol

            elif temp_check == 0:
                if temp_r < 0:
                    new_r = (-temp_r)**(1/3)
                else:
                    new_r = temp_r**(1/3)

                sol[0]["real"] = -first_term+2*new_r
                sol[1]["real"] = -(new_r+first_term)
                sol[2]["real"] = sol[1]["real"]

                return sol

            else:
                temp2 = acos(temp_r/(-temp_q*-temp_q*-temp_q)**0.5)
                temp = -first_term + 2*temp_q**0.5

                sol[0]["real"] = temp*cos(temp2/3)
                sol[1]["real"] = temp*cos((temp2+2*pi)/3)
                sol[2]["real"] = temp*cos((temp2+4*pi)/3)
                return sol

        elif degree == 4:
            pass

    def __str__(self) -> str:
        return self.string_form


# p1 = Polynomial("x^2+2x+1", fracmode=True)
# p2 = Polynomial("x^2+2x+1", fracmode=False)

# print(p1.solve())

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)