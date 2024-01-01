#TABULATION APPROACH
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = {}
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        n = len(cost)
        for i in range(2, n):
            min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])
        min_cost[n] = min(min_cost[n-1], min_cost[n-2])
        return min_cost[n]

#DONE (REVIEW LATER)