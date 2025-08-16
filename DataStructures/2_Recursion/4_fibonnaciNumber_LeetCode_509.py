"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Leetcode: https://leetcode.com/problems/fibonacci-number/description/
"""
class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 0 or n == 1:
            return n
        # recursive case
        return self.fib(n-1) + self.fib(n-2)


s1 = Solution()

print(s1.fib(6))    # 8