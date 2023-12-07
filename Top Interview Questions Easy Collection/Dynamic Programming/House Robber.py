class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums)
        V_0 = 0
        V_1 = nums[0]
        for i in range(1,L):
            V_0_C = max(V_1, V_0)
            V_1_C = nums[i] + V_0   
            V_0 = V_0_C
            V_1 = V_1_C       
        return max(V_0,V_1)  
