class Solution(object):
    def isValid(self, s):
        myStack = []
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                myStack.append(s[i])
            else:
                if len(myStack) == 0:
                    return False
                if s[i] == ')' and myStack[-1] == '(':
                    myStack.pop()
                elif s[i] == '}' and myStack[-1] == '{':
                    myStack.pop()
                elif s[i] == ']' and myStack[-1] == '[':
                    myStack.pop()
                else:
                    return False
        if len(myStack) == 0:
            return True
        