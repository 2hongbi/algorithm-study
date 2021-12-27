import math


def average(lst):
    return int(sum(lst) / len(lst))


def min_error(mean, lst):
    min_error_sum = 0
    for l in lst:
        min_error_sum += int(math.pow((mean - l), 2))
    return min_error_sum


def main():
    in_list = list(map(int, input().split()))

    # sort
    in_list.sort()
    print(in_list)

    output = []
    temp_list = []
    for idx, item in enumerate(in_list):
        if idx == 0:
            temp_list.append(item)
        else:
            temp = in_list[idx - 1]
            bt_error = (item - temp)
            if bt_error <= 10:
                temp_list.append(item)
            else:
                output.append(temp_list)
                temp_list = [item]
    output.append(temp_list)

    print('>> LIST GROUP :', output)

    # get min square error from each group

    mse_list = [min_error(average(out), out) for out in output]
    print('>> LIST GROUP : {0}, Min value : {1}'.format(mse_list, min(mse_list)))

    return min(mse_list)


if __name__ == '__main__':
    main()