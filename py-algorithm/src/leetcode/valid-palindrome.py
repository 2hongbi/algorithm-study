import collections
import re
from typing import Deque


def is_palindrome1(s):
    # use list
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # determine palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def is_palindrome2(s: str) -> bool:
    # declare deque as data type
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome3(s: str) -> bool:
    # using slicing
    s = s.lower()
    # remove unnecessary character
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]  # slicing


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome1(s))
    print(is_palindrome2(s=s))
    print(is_palindrome3(s))