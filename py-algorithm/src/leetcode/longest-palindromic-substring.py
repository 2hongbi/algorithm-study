def longest_palindrome(s: str) -> str:
    # distinguish palindrome and expand two pointer
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    # when there is no
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    # move right with sliding window
    for i in range(len(s) - 1):
        result = max(result, expand(i, i+1),
                     expand(i, i+2), key=len)
    return result


if __name__ == '__main__':
    s = 'babad'
    print(longest_palindrome(s))