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
import copy


def mk_moo(num):
    moo_seq = ['m']
    if num == 0:
        return ['m', 'o', 'o']
    for i in range(num+2):
        moo_seq.append('o')
        i += 1
    return moo_seq


def mk_seq(num, seq1, seq2):
    seq1.extend(mk_moo(num))
    seq1.extend(seq2)
    return seq1


def moo_sequence():
    seq = mk_moo(0)
    s0 = mk_moo(0)
    mk_seq(1, seq, s0)  # seq 생성
    s1 = copy.deepcopy(seq)
    mk_seq(2, seq, s1)  # seq 생성
    s2 = copy.deepcopy(seq)
    mk_seq(3, seq, s2)  # seq 생성
    s3 = copy.deepcopy(seq)
    mk_seq(4, seq, s3)
    return seq


def moo(num):
    if num == 0:
        return 'moo'
    else:
        return moo(num-1) + 'm' + 'o' * (num+2) + moo(num-1)


if __name__ == '__main__':
    N = int(input())

    # 첫 번째 : 노가다
    # print(moo_sequence()[num-1])

    # 두 번째 : factorial 수열
    print(moo(4)[N-1])

    # 개선 방향 : 무한 수열임을 이용할 것