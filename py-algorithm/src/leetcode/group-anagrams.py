import collections
from typing import List


def group_anagrams(strs: List[str]) -> list[list]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # sort and add to dictionary
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


if __name__ == '__main__':
    str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(str_list))