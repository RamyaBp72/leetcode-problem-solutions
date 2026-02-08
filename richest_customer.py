class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        max_wealth = 0
        for customers in accounts:
         max_wealth = max(max_wealth,sum(customers))   
        
        return max_wealth
