import collections


# check report
def solution(id_list, report, k):
    answer = []
    report = set(report)

    report_dic = collections.defaultdict(list)
    count_dic = collections.defaultdict(int)

    for r in report:
        reporter, reported = r.split()
        report_dic[reporter].append(reported)
        count_dic[reported] += 1

    print(count_dic)
    print(report_dic)

    for id in id_list:
        result = 0
        for report in report_dic[id]:
            if count_dic[report] >= k:
                result += 1
        answer.append(result)
    return answer


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    print(solution(id_list, report, k=2))
    print(solution2(id_list, report, k=2))