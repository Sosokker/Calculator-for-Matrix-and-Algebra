from math import gcd

class Fraction:
    def __init__(self, numer, denom):
        if numer < 0 and denom < 0:
            numer = -numer
            denom = -denom
        if denom < 0:
            numer = -numer
            denom = -denom
        if denom == 0:
            raise ValueError("Denominator shouldn't be zero.")
        self.__numer = numer
        self.__denom = denom
        self.floating = numer/denom

    @property
    def numer(self):
        return self.__numer

    @property
    def denom(self):
        return self.__denom
    
    @numer.setter
    def numer(self, value):
        self.__numer = value

    @denom.setter
    def denom(self, value):
        if value < 0:
            self.__numer = -self.numer
            self.__denom = -value
        if value == 0:
            raise ValueError("Denominator shouldn't be zero.")
        self.__denom = value

    def __add__(self, other):
        """
        Add Fraction.
        >>> m1 = Fraction(2, 3)
        >>> m2 = Fraction(5, 7)
        >>> m3 = m1 + m2
        >>> print(m3)
        29/21
        """
        denom = self.denom * other.denom
        numer = self.numer*other.denom + other.numer*self.denom
        result = Fraction(numer, denom)
        return result
       

    def __sub__(self, other):
        """
        Substract Fraction.
        >>> m1 = Fraction(2, 3)
        >>> m2 = Fraction(5, 7)
        >>> m3 = m1 - m2
        >>> print(m3)
        -1/21
        """
        denom = self.denom * other.denom
        numer = self.numer*other.denom - other.numer*self.denom
        result = Fraction(numer, denom)
        return result

    def __mul__(self, other):
        """
        Multiply Fraction.
        >>> m1 = Fraction(2, 3)
        >>> m2 = Fraction(5, 7)
        >>> m3 = m1 * m2
        >>> print(m3)
        10/21
        """
        denom = self.denom * other.denom
        numer = self.numer * other.numer
        result = Fraction(numer, denom)
        return result

    def __truediv__(self, other):
        """
        Divide Fraction with other one.
        >>> m1 = Fraction(2, 3)
        >>> m2 = Fraction(5, 7)
        >>> m3 = m1 / m2
        >>> print(m3)
        14/15
        """
        denom = self.denom * other.numer
        numer = self.numer * other.denom
        result = Fraction(numer, denom)
        return result

    def __pow__(self, other):
        """
        Power Fraction.
        >>> m1 = Fraction(2, 3)
        >>> m2 = 2
        >>> m3 = m1**m2
        >>> print(m3)
        4/9
        >>> m1 = Fraction(-2, 3)
        >>> m2 = 2
        >>> m3 = m1**m2
        >>> print(m3)
        4/9
        >>> m1 = Fraction(-2, 3)
        >>> m2 = 3
        >>> m3 = m1**m2
        >>> print(m3)
        -8/27
        >>> m1 = Fraction(-2, 3)
        >>> m2 = -3
        >>> m3 = m1**m2
        >>> print(m3)
        -27/8
        """
        if isinstance(other, int):
            if other > 0:
                numer = self.numer**other
                denom = self.denom**other
                return Fraction(numer, denom)
            elif other == 0:
                return 1
            elif other < 0:
                numer = self.numer**(-other)
                denom = self.denom**(-other)
                return Fraction(denom, numer)

    def reduce_frac(self):
        """
        Turn Fraction into reduce form.
        >>> m1 = Fraction(2, 4)
        >>> m1.reduce_frac()
        >>> print(m1)
        1/2
        """
        temp = gcd(self.numer, self.denom)
        self.numer = self.numer // temp
        self.denom = self.denom // temp

    def __str__(self) -> str:
        """
        Print Fraction Form.
        >>> m1 = Fraction(1, 2)
        >>> print(m1)
        1/2
        >>> m2 = Fraction(5, -2)
        >>> print(m2)
        -5/2
        >>> m3 = Fraction(-5, 2)
        >>> print(m3)
        -5/2
        >>> m4 = Fraction(-5, -2)
        >>> print(m4)
        5/2
        """
        if self.numer == 0:
            return "0"
        return f"{self.numer}/{self.denom}"