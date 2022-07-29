def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]  # num of answers

    zero_cnt = lottos.count(0)
    win_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1

    return [rank[win_cnt + zero_cnt], rank[win_cnt]]


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))

    lottos3 = [45, 4, 35, 20, 3, 9]
    win_nums3 = [20, 9, 3, 45, 4, 35]
    print(solution(lottos3, win_nums3))