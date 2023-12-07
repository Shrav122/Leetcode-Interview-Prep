class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # solution1
        nums = nums + list(range(0,len(nums)+1))
        ans = 0
        for i in nums:
            ans ^= i
        return ans

        # solution2
        # return (list(set(range(0,len(nums)+1)) - set(nums)) or [0])[0]

        # solution3
        # return sum(range(0,len(nums)+1)) -sum(nums)



     



     



     