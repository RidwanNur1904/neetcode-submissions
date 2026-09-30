class Solution:
    def isValid(self, s: str) -> bool:
        #for questions like this its to assume that it would be a stack
        stack = []
        lookup = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        #check to see if the brackets are actually in the thing
        for bracket in s:
            #an empty list/dictionary means false
            if bracket in lookup.values():
                stack.append(bracket)
                #something something top of the stack
                #the top of the stack is like -1 and second top is -2 so on and so on
            elif not stack or stack[-1] != lookup[bracket]:
                return False
            else: stack.pop()

        return not stack
            