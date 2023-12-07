class Solution:
    def fib(self, n: int) -> int:
        current_val = 0
        next_val = 1
        if n == 0:
            return current_val
        elif n == 1:
            return next_val
        else:
            for i in range(2, n + 1):
                sum = current_val + next_val
                current_val = next_val
                next_val = sum

            return next_val

        