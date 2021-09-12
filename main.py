# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def calPoints(self, ops) -> int:
        stack = []
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * int(stack[-1]))
            elif op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(op))
        return sum(stack)


ops = ["1"]
test = Solution()
print(test.calPoints(ops))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
