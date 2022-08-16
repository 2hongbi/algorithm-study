from typing import List


def array_pair_sum(nums: List[int]) -> int:
    # using ascending sort
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # calculate the sum by creating pairs in ascending order from the front
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def array_pair_sum2(nums: List[int]) -> int:
    sums = 0
    nums.sort()

    for i, n in enumerate(nums):
        # calculate the sum of even-numbered values
        if i % 2 == 0:
            sums += n

    return sums


def array_pair_sum3(nums: List[int]) -> int:
    # use pythonic way
    return sum(sorted(nums)[::2])



if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(array_pair_sum(nums))
    print(array_pair_sum2(nums))