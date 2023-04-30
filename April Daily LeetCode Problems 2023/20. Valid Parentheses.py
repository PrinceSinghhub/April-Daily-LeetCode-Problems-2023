# lc : https://leetcode.com/problems/valid-parentheses/
# gfg: https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
class Solution:
    def isValid(self, s):

        Stack = []
        for i in s:
            if i in ['(', '{', '[']:
                Stack.append(i)

            elif i == ')' and len(Stack) != 0 and Stack[-1] == '(':
                Stack.pop()

            elif i == '}' and len(Stack) != 0 and Stack[-1] == '{':
                Stack.pop()

            elif i == ']' and len(Stack) != 0 and Stack[-1] == '[':
                Stack.pop()

            else:
                return False

        if len(Stack) == 0:
            return True


