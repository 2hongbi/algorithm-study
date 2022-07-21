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


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome1(s))