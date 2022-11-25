class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.floating = numer/denom

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
        return f"{self.numer}/{self.denom}"