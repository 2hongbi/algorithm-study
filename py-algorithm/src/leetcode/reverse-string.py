from typing import List


class Solution(object):
    def reverse_string(s: List[str]) -> None:
        """
        :type s: List[str]
        :return: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse_string2(s: List[str]) -> None:
        s.reverse()


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(Solution.reverse_string(s))
    print(Solution.reverse_string2(s))