class PrepareExpression:
    @staticmethod
    def add_asterisks(expression):
        result = ""

        for i in range(len(expression)):
            char = expression[i]
            if char.isdigit() and i < len(expression) - 1 and expression[i + 1] == "(":
                result += char + "*"
            elif char == ")" and i < len(expression) - 1 and expression[i + 1] == "(":
                result += char + "*"
            else:
                result += char

        return result

    @staticmethod
    def fix_mismatched_parentheses(expression):
        stack = []
        result = ""
        opening_parentheses_count = 0

        for char in expression:
            if char == "(":
                stack.append(char)
                opening_parentheses_count += 1
            elif char == ")":
                if stack:
                    stack.pop()
                    opening_parentheses_count -= 1
                else:
                    # Ignore the extra closing parenthesis
                    continue
            result += char

        result += opening_parentheses_count * ")"

        return result






