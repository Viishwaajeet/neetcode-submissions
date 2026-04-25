class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def solve(op1, op2, operator):
            if operator == "+":
                return op1+op2
            elif operator == "-":
                return op1-op2
            elif operator == "*":
                return op1*op2
            elif operator == "/":
                return int(op1/op2)
        
        stack = []
        for i in tokens:
            if i in "+-*/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(solve(op1,op2,i))
            else:
                stack.append(int(i))

        return stack[0]