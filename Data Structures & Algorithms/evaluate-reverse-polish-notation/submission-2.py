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
                return op1/op2
        
        stack = []
        operators = ["+","-","*","/"]
        i = 0
        while i<len(tokens):
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))
            elif tokens[i] in operators:
                op1 = stack.pop(len(stack)-1)
                op2 = stack.pop(len(stack)-1)
                stack.append(solve(op1,op2,tokens[i]))
            i+=1

        return stack[0]