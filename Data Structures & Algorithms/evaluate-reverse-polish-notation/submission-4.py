class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 
        operands = {'+', '-', '*', '/'}

        stack = []
        i = 0
        while i < len(tokens):
            if stack and tokens[i] in operands:
                operand = tokens[i]
                b = int(stack.pop())
                a = int(stack.pop())

                if operand == '+':
                    res = a + b
                elif operand == '-':
                    res = a - b
                elif operand == '*':
                    res = a * b
                else:
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(int(tokens[i]))
            i += 1

        return stack[0]

                

                


        