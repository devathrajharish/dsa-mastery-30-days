def max_profit(prices):
    """
    Track the cheapest buy price seen so far; at each day,
    check profit if we sold today.
    Time: O(n), Space: O(1)
    """
    min_price = float('inf')
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best

## One line solution using built-in min and max functions
    return max(prices) - min(prices)

if __name__ == "__main__":
    prices = [7,1,5,233,6,4]
    print(max_profit(prices))