from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # product left side
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # multiply the result by the right value sequentially
    for i in range(len(nums) - 1, 0 - 1, -1):
        print('i : ',  i)
        out[i] = out[i] * p
        p = p * nums[i]
    return out


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))