class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        while len(s)>0:
            if s[-1] in ")}]":
                stack += s[-1]
                s = s[:-1]
            elif s[-1] in "([{":
                if len(stack)==0:
                    return False
                elif s[-1]=="(" and stack[-1]==")":
                    stack = stack[:-1]
                    s = s[:-1]
                elif s[-1]=="[" and stack[-1]=="]":
                    stack = stack[:-1]
                    s = s[:-1]
                elif s[-1]=="{" and stack[-1]=="}":
                    stack = stack[:-1]
                    s = s[:-1]
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False