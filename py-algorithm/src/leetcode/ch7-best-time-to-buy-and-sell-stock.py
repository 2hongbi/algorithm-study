import sys
from typing import List


def max_profit(prices: List[int]) -> int:
    # using brute-force (but time-out)
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    return max_price


def max_profit2(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # update minimum and maximum values
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]