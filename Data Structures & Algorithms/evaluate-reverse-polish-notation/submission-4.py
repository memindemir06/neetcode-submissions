class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(operand1, operand2, operator):
            if operator == "+":
                return int(operand1) + int(operand2)
            if operator == "-":
                return int(operand1) - int(operand2)
            if operator == "/":
                return int(float(operand1) / int(operand2))
            if operator == "*":
                return int(operand1) * int(operand2)
            else:
                raise "Operator not defined"
        
        operands = []
        operators = set(['+', '-', '*', '/'])

        while len(tokens) > 0:
            token = tokens.pop(0)

            if token in operators:
                operand1 = operands.pop()
                operand2 = operands.pop()
                result = evaluate(operand2, operand1, token)

                operands.append(result)
            else:
                operands.append(token)

        return int(operands[0])

        