"""
기능 개발  https://programmers.co.kr/learn/courses/30/lessons/42586
각 기능은 진도가 100%일 때 배포 가능
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있으나, 뒤에 있는 기능은 앞에 있는 모든 기능이 완성될 때 함께 배포 가능
입력:
    - 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 	  (배포 순서대로 각 기능마다의 작업 진도) progresses
    - 각 기능의 개발 속도가 적힌 정수 배열
        (하루마다의 진도율) speeds
출력:
    - 각 배포마다 몇 개의 기능이 배포되는지를 return
각 기능은 한번만 배포
작업의 개수(progresses, speeds배열의 길이)는 100개 이하
작업 진도(progresses 배열 원소): 100 미만의 자연수
작업 속도(speeds 배열 원소): 100 이하의 자연수
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정
    ex) 진도율: 95%, 개발 속도: 4%
    1일: 99%, 2일: 103%로 2일 뒤에 배포
** 가장 중요한 것 : 각 기능은 반드시 앞에 있는 모든 기능이 완성되어야 배포 가능
"""


def func_develop(progresses, speeds):
    build = []
    days, count = 0, 0
    while len(progresses) > 0:
        if (progresses[0] + days*speeds[0]) >= 100:   # 90 + time * 1 --> time = 10
            progresses.pop(0)  # 다음 태스크로 넘어감
            speeds.pop(0)  # 다음 태스크의 속도로 넘어감
            count += 1  # 완료된 태스크 추가
        else:  # 100%가 안된 경우
            if count > 0:
                build.append(count)
                count = 0  # 초기화
            days += 1
    build.append(count)  # 마지막 count 추가 위함
    return build


if __name__ == "__main__":
    print(func_develop([93, 30, 55], [1, 30, 5]))
    print(func_develop([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))