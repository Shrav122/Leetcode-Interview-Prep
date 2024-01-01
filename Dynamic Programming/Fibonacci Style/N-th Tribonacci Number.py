#BRUTE-FORCE
#Time limit exceeding for 7/39 test cases, including n = 31, and other test cases successfully passed (I believe time limit exceeds for large inputs, according to an online source, recursion approach takes longer time for large inputs)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

#MEMOIZATION - WORKS SUCCESSFULLY
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        return self.calc_trib(n, memo)

    def calc_trib(self, n: int, memo: dict) -> int:
        if n == 0 or n == 1 or n == 2:
            return memo[n]
        elif n not in memo:
            memo[n] = self.calc_trib(n-1, memo) + self.calc_trib(n-2, memo) + self.calc_trib(n-3, memo)
        return memo[n]  

#DONE


#WORKS BUT TAKES MORE AND MORE TIME TO GET BACK