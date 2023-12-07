class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        transactions = [[1000, 0] for i in range(k)]

        for price in prices:
            prev_profit = 0
            for i in range(k):
                transactions[i][0] = min(transactions[i][0], price - prev_profit)
                transactions[i][1] = max(transactions[i][1], price - transactions[i][0])
                prev_profit = transactions[i][1]

        return transactions[k-1][1]