def div(a, b):
        return int(a/b) if (a * b) > 0 else -(abs(a)// abs(b))
from operator import add, sub, mul
class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': div}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(self.op_map[token](num2, num1))
        return stack.pop()
