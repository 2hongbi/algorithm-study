"""
    <선분 교차>
    2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 알아보기
    - 선 L1 : x1, y1, x2, y2
    - 선 L2 : x3, y3, x4, y4
    -1,000,000 <= x1, x2, x3, x4, y1, y2, y3, y4 <= 1,000,000이며, 변수는 모두 정수
    L1과 L2가 교차하면 1
    L2와 L2가 교차하지 않으면 0
"""


def does_it_divide(x1, y1, x2, y2, x3, y3, x4, y4):
    f1 = (y3-y1)*(x2-x1) - (x3-x1)*(y2-y1)
    f2 = (y4-y1)*(x2-x1) - (x4-x1)*(y2-y1)
    if f1 * f2 < 0:
        return True
    else:
        return False


def does_it_intersect():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    result1 = does_it_divide(x1, y1, x2, y2, x3, y3, x4, y4)
    result2 = does_it_divide(x1, y1, x2, y2, x3, y3, x4, y4)

    if result1 and result2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(does_it_intersect())