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
        
        op1, op2 = int(tokens[0]), int(tokens[1])
        operators = ["+","-","*","/"]
        i = 2
        while i<len(tokens):
            if tokens[i] in operators:
                op1 = solve(op1,op2,tokens[i])
            elif tokens[i].isdigit():
                op2 = int(tokens[i])
            i+=1
        
        return op1
