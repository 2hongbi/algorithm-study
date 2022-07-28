from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    # use lambda and '+' operator
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # sort 2 keys with lambda expression
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let 1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorder_log_files(logs))