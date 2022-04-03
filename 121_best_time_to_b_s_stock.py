# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Input: prices = [7,1,5,3,6,4]
# Output: 5 

#------------------------------------

# given a list of day prices
# set the defauly max profit
# iterate through the list of prices
#   iterate through all the values following the initial value
#     check and calculate the value by subtracting following day from current dat
#       if the profit of a set day is greater than the max profit, replace max profit
#       if the profit for a day is not greater than max profile, dont do anything
# return max_profilt

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit

