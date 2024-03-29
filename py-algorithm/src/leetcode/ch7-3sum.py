from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # using brute force
    results = []
    nums.sort()

    # iterate brute force for n^3 times
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            # pass duplicated values
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


def three_sum2(nums: List[int]) -> List[List[int]]:
    # using two-pointer
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # pass duplicated values
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < 0:
                left += 1
            elif sums > 0:
                right -= 1
            else:
                # add to result and skip to next level
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
    print(three_sum2(nums))