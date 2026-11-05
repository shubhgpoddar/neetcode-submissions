class Solution:
    def isValid(self, s: str) -> bool:
        '''
        5:19 
        Algorithm:
        - string contains only brackets
        Stack: FILO/ LIFO
        - If opening bracket push to stack
        - If closing: pop from the end of the stack.
        - if values are unequal return False.
        e.g "([{}])"
        stack = (
        '''

        brackets = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch not in brackets:
                stack.append(ch)
            else:
                if not stack: return False
                if stack.pop(-1)!=brackets[ch]:
                    return False
        return len(stack)==0