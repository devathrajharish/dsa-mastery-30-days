"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You want to maximize profit by choosing a single day to buy
and a different day in the future to sell.
Return the maximum profit. If no profit, return 0.
"""

from typing import List


def max_profit_bruteforce(prices: List[int]) -> int:
    """
    Brute Force - Check all pairs
    Time: O(n²) - All pairs of days
    Space: O(1)

    For each day, check all future days and find max profit.
    """
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


def max_profit_optimized(prices: List[int]) -> int:
    """
    Optimized - One pass with tracking minimum
    Time: O(n) - Single pass
    Space: O(1)

    Key Insight: Track minimum price seen so far.
    For each price, calculate profit from minimum.
    This is the best we can do without looking ahead!
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Calculate profit if we sell at current price
        profit = price - min_price
        max_profit = max(max_profit, profit)

        # Update minimum if current price is lower
        min_price = min(min_price, price)

    return max_profit


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),      # Prices only decrease
        ([2, 4, 1, 7, 5, 11], 10), # Buy at 1, sell at 11
        ([1], 0),                   # Single day
    ]

    for prices, expected in test_cases:
        result = max_profit_optimized(prices.copy())
        status = "✅" if result == expected else "❌"
        print(f"{status} Prices: {prices} -> Profit: {result} (Expected: {expected})")

    # Complexity Analysis
    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n²), Space O(1)")
    print("Optimized:   Time O(n),  Space O(1)")

    # Trace example
    print("\n🔍 Trace Example: [7, 1, 5, 3, 6, 4]")
    prices = [7, 1, 5, 3, 6, 4]
    min_price = prices[0]
    print(f"Start: min_price = {min_price}, max_profit = 0")

    for price in prices[1:]:
        profit = price - min_price
        print(f"  Price: {price}, Profit if sell: {profit}, "
              f"New min: {min(min_price, price)}")
        min_price = min(min_price, price)
