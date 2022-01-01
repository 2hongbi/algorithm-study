def my_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def my_sum2(args, idx=None):
    total = 0
    for arg in args:
        total += arg
    if idx:
        total = total + idx
    return total


def my_avg(args):
    return sum(args) / len(args)


def my_word_sts(args):
    len_list = [len(arg) for arg in args]
    return (min(len_list), max(len_list), sum(len_list) / len(len_list))    # tuple


def my_diverse_sum(args):
    total = 0
    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            print('>> String cannot be transformed to integer.')
            pass
    return total


if __name__ == '__main__':
    print(my_sum(1, 2, 3, 4))
    print(my_sum(*[10, 20, 30, 40]))
    print(my_sum2([1, 2, 3]))
    print(my_sum2([1, 2, 3], 4))
    print(my_avg([1, 2, 3, 4]))
    print(my_word_sts(['나비', '뱀', '독수리', '까마귀', '아이스크림']))
    print(my_diverse_sum(['1', 2, 'python', 3, '4', '100', 'hello']))

