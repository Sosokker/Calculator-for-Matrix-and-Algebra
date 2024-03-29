import sys
import pytest
sys.path.append('..')

from src.preparer.PrepareExpression import PrepareExpression

def test_add_asterisks():
    preparer = PrepareExpression()

    # Test case 1: Single level parentheses
    expression1 = "(1+2)(3+4)"
    result1 = preparer.add_asterisks(expression1)
    assert result1 == "(1+2)*(3+4)"

    # Test case 2: Nested parentheses
    expression2 = "(1+2(2+3(3+4)))"
    result2 = preparer.add_asterisks(expression2)
    assert result2 == "(1+2*(2+3*(3+4)))"

def test_fix_mismatched_parentheses():
    preparer = PrepareExpression()

    # Test case 1: Fixing a single mismatched closing parenthesis
    expression1 = "(((1+2)+3)+4))"
    fixed_expression1 = preparer.fix_mismatched_parentheses(expression1)
    assert fixed_expression1 == "(((1+2)+3)+4)"

    # Test case 2: Fixing a single mismatched opening parenthesis
    expression2 = "(((1+2)+3)+4"
    fixed_expression2 = preparer.fix_mismatched_parentheses(expression2)
    assert fixed_expression2 == "(((1+2)+3)+4)"

    # Test case 3: Fixing multiple mismatched parentheses
    expression3 = "(((1+2)+3)+4))"
    fixed_expression3 = preparer.fix_mismatched_parentheses(expression3)
    assert fixed_expression3 == "(((1+2)+3)+4)"

    # Test case 4: No mismatched parentheses
    expression4 = "(((1+2)+3)+4)"
    fixed_expression4 = preparer.fix_mismatched_parentheses(expression4)
    assert fixed_expression4 == "(((1+2)+3)+4)"

def test_combined_methods():
    preparer = PrepareExpression()

    # Test case 1: Combined methods: add_asterisks + fix_mismatched_parentheses
    expression1 = "(((1+2)+3)+4))"
    result1 = preparer.add_asterisks(expression1)
    fixed_result1 = preparer.fix_mismatched_parentheses(result1)
    assert fixed_result1 == "(((1+2)+3)+4)"


if __name__ == '__main__':
    pytest.main()
