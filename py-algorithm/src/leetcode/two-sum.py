from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # using brute-force - very inefficient
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum2(nums: List[int], target: int) -> List[int]:
    # using in
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


def two_sum3(nums: List[int], target: int) -> List[int]:
    # Retrieve the result of subtracting the first number
    nums_map = {}
    # swap key and values and store them as a dictionary
    for i, num in enumerate(nums):
        nums_map[num] = i
    # Retrieve the result of subtracting the first number from the target as a key
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


def two_sum4(nums: List[int], target: int) -> List[int]:
    # Improved structure
    nums_map = {}
    # Integrated into one for statement
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


def two_sum5(nums: List[int], target: int) -> List[int]:
    # Using two pointer (need to sort)
    nums.sort()    # index is messed up, so we can't use this algorithm in this problem.
    left, right = 0, len(nums) - 1
    while not left == right:
        # if the sum is less than target, move the left pointer to the right
        if nums[left] + nums[right] < target:
            left += 1
        # if the sum is greater than target, move the right pointer to the left
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
    print(two_sum4(nums, target))
    print(two_sum5(nums, target))  # can't use