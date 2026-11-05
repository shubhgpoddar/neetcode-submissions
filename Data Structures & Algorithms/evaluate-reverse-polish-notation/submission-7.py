class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        5:29
        Expressions are always valid
        Algorithm:
        1. Use a stack FILO but preserve the ordering of operands
        2. If operand, push to stack.
        3. If operator, pop 2 elements, perform arithematic and push to stack
        e.g ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        [17 5]
        '''
        operators = {'+', '-', '*', '/'}
        stack = []

        for ch in tokens:
            if ch not in operators:
                stack.append(ch)
            else:
                opB = int(stack.pop(-1))
                opA = int(stack.pop(-1))
                if ch == '+':
                    val = opA + opB
                elif ch == '-':
                    val = opA - opB
                elif ch == '*':
                    val = opA*opB
                elif ch == '/':
                    val = int(opA / opB)
                stack.append(str(val))
                
        return int(stack[0])
            
        