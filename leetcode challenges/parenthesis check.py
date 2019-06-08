def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    opening_list = ['(', '[', '{']
    closing_list = [')', ']', '}']
    arr = list()
    stack = list()
    result = False
    arr = [str(r) for r in s]
    if len(arr) == 1:
        result = False
    if len(arr) == 0:
        result = True
    else:
        for index, c in enumerate(arr):

            if ((c == '(') or (c == '{') or (c == '[')):
                stack.append(c)
            # compare the last element of stack and next of array to pop
            if ((len(stack) >= 1) and (((c == ')') and (stack[-1] != '(')) or ((c == '}') and (stack[-1] != '{')) or (
                    (c == ']') and (stack[-1] != '[')))):
                result = False
                break
            if ((len(stack) >= 1) and (((c == ')') and (stack[-1] == '(')) or ((c == '}') and (stack[-1] == '{')) or (
                    (c == ']') and (stack[-1] == '[')))):
                stack.pop()
                result = True
            else:
                result = False
        if (len(stack) != 0):
            result = False
    return result



##########################################################################################
    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            opening_list = ['(', '[', '{']
            dict = {")": "(", "}": "{", "]": "["}
            arr = list()
            stack = list()
            arr = [str(r) for r in s]
            for c in arr:
                if (c in opening_list):
                    stack.append(c)
                elif not stack:
                    return False
                elif ((dict[c] != stack.pop())):
                    return False
            return not stack
