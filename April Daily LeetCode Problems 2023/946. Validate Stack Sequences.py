class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []

        index = 0

        n = len(pushed)

        for item in pushed:

            stack.append(item)

            while len(stack) > 0 and index < n and stack[-1] == popped[index]:
                stack.pop()

                index += 1

        return index == n
