"""
    Moo 게임(상)
    https://www.acmicpc.net/problem/5904
    재귀적이고 길이가 무한대인 수열
    S(k) = S(k-1) + [“m” + “o” * (k+2)] + S(k-1)
    S(0) = "m o o"
    S(1) = "m o o m o o o m o o" = "m o o" + "m o o o" + "m o o"
        = S(0) + "o"가 (1(k)+2)개인 수열 "m o o o" + S(0)
    S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"
        = "m o o m o o o m o o" + "m o o o o" + "m o o m o o o m o o“
        =  S(1) + "o"가 (2(k)+2)개인 수열 "m o o o o" + S(1)
    - 입력: N (1 ≤ N ≤ 109)
    - 출력: Moo 수열의 N번째 글자
    - 11 입력시, m 출력
"""


def mk_moo_seq(num):
    moo_seq = []
    s0 = ['m', 'o', 'o']
    if num == 0:
        return s0
    else:
        for i in num:
            continue
    return


def moo_game():
    n = int(input())

    moo_list = ['m', 'o', 'o']
