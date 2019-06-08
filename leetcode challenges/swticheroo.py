# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#


def get_switch(argument):
    switcher={
    1:"one",
    2:"two"
    }
    return switcher.get(argument, "nothing")

if __name__=="__main__":
    argument=1
    print (get_switch(0))

#-------------------------------------------------
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = list()
        stack = list()
        result=False
        arr = [str(r) for r in s]
        if len(arr)==0:
            result=True
        else:
            for index, c in enumerate(arr):
                # if ((c == '(') or (c == '{') or (c == '[')):
                #     stack.append(c)
                if ((c[index-1]=='(')and(c == ')')):
                    #stack.pop()
                    print("ok")
        return len(stack) == 0


#or (c == '}') or (c == ']')