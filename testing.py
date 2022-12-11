from nessesary.polynomial import Polynomial
from nessesary.fraction import frac_of_float, Fraction, to_fraction
from nessesary.matrix import Matrix
from nessesary.parser.parser import insert_mul_sign, parse_poly
from nessesary.equation.processing import poly_expand, solver, simplify, change_side

# -------------------------- POLYNOMIAL TEST --------------------------


p1 = Polynomial("x^3+3112+1231+x^2+2131+x^3")
p2 = Polynomial([1,2,3,4,5,6,7,8,9,10])
p3 = Polynomial([4,3,2,3,4])
p4 = Polynomial("-4x^9 + 32x^4 +1212 -5x^2 +5x^9")
p5 = Polynomial("-4x^9 + 1")
p6 = Polynomial("x+1")
p7 = Polynomial("3x^2-2x^2+2x+1")

assert str(p1) == "2x^3+1x^2+6474"
assert str(p2) == "10x^9+9x^8+8x^7+7x^6+6x^5+5x^4+4x^3+3x^2+2x+1"
assert str(p3) == "4x^4+3x^3+2x^2+3x+4"
assert str(p4) == "x^9+32x^4-5x^2+1212"
assert str(p5) == "-4x^9+1"
assert str(p6) == "1x+1"
assert str(p7) == "x^2+2x+1"
assert Polynomial("3x+2").to_str() == "3x+2"

assert p7.solve() == [{'real': -1.0, 'imag': 0}]
assert Polynomial("x+1").solve() == [{'real': -1.0, 'imag': 0}]
assert Polynomial("x+3123 -312321312+281x-32131x").solve() == [{'real': -9806.21649031366761, 'imag': 0}]
assert Polynomial("23x^2-312x+321x^2-3+6+0+0").solve() == [{'real': 0.009719543319502776, 'imag': 0}, {'real': 0.8972572008665437, 'imag': 0}]


# -------------------------- FRACTION TEST --------------------------

assert frac_of_float(0.22131321, reduce=False) == 22131321/100000000
assert frac_of_float(0.22131322, reduce=True) == 11065661/50000000
assert Fraction(10,100).floating == 0.1
assert str(Fraction(5311,321231)) == '5311/321231'
p1 = Fraction(521,21244) # 521/21244
p2 = Fraction(-3321,21231) # -3321/21231
p3 = p1-p2
p3.reduce_frac()

assert str(p3) == str(Fraction(9068075, 50114596))
