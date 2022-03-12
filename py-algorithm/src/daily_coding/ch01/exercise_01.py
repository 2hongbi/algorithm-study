import random


def guessing_game():
    answer = random.randint(0, 100)

    while True:
        my_answer = int(input('숫자를 맞춰보세요! : '))

        if my_answer > answer:
            print(f'* {my_answer}는 너무 큽니다.')
        elif my_answer < answer:
            print(f'* {my_answer}는 너무 작습니다.')
        elif my_answer == answer:
            print(f'>> 정답은 {my_answer}입니다!')
            break

    print('프로그램을 종료합니다')


def guessing_game_within_3_times():
    # 사용자가 숫자를 예측해볼 기회를 3번까지로 제한
    answer = random.randint(0, 100)

    i = 0
    while True:
        if i == 3:
            print('기회 초과!')
            break

        my_answer = int(input(f'{i+1}번째 시도 > 숫자를 맞춰보세요! : '))

        if my_answer > answer:
            print(f'* {my_answer}는 너무 큽니다.')
        elif my_answer < answer:
            print(f'* {my_answer}는 너무 작습니다.')
        elif my_answer == answer:
            print(f'>> 정답은 {my_answer}입니다!')
            break

        i += 1
    print('프로그램을 종료합니다')


def guessing_string_game():
    # 단어(문자열) 맞히기 게임
    str_list = [
        'apple', 'bus', 'cat', 'dog', 'elephant', 'fox', 'guess', 'high', 'ice', 'juice', 'korea'
    ]

    answer_index = random.randint(0, len(str_list)-1)
    answer = str_list[answer_index]

    while True:
        my_answer = input(f'{str_list} 중 정답을 맞춰주세요! : ')

        if my_answer == answer:
            print('>> 정답입니다!')
            break

        if str_list.index(my_answer) > answer_index:
            print('>>> 답은 더 앞쪽에 있습니다.')
        else:
            print('>>> 답은 더 뒤쪽에 있습니다.')


if __name__ == '__main__':
    # guessing_game()
    guessing_string_game()