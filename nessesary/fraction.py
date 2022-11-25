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
        if denom < 0:
            numer = -numer
            denom = -denom
        if denom == 0:
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
        return f"{self.numer}/{self.denom}"