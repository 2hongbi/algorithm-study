from typing import List


def trap(height: List[int]) -> int:
    # using two pointer
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # move the two-pointer towards higher
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        return volume


def trap2(height: List[int]) -> int:
    # use stack
    stack = []
    volume = 0

    for i in range(len(height)):
        # if meets inflection point
        while stack and height[i] > height[stack[-1]]:
            # pop stack
            top = stack.pop()

            if not len(stack):
                break

            # treat the water level by the difference from before
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))
    print(trap2(height))