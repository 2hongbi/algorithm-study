import re


def solution(new_id):
    # 1. convert uppercase to lowercase
    answer = new_id.lower()
    # 2. remove characters except lowercase, num, -, _, .
    answer = re.sub('[^a-z0-9\-\_\.]', '', answer)
    # 3. if new_id contains continuous periods, replace only one period
    answer = re.sub(r'\.{2,}', '.', answer)
    # 4. remove periods at both ends
    answer = answer.strip('.')
    # 5. if answer is empty string, then substitute answer 'a'
    if len(answer) == 0:
        answer = 'a'
    # 6. if length of answer is 16 or more, truncate to answer 15
    if len(answer) > 15:
        answer = answer[:15].rstrip('.')
    # 7. if length of answer is 2 or less, concatenate the last character of answer until the length is 3
    while len(answer) < 3:
        answer += answer[-1]
    return answer


if __name__ == '__main__':
    s = '...!@BaT#*..y.abcdefghijklm'
    print(solution(s))