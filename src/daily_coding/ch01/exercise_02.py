def my_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


if __name__ == '__main__':
    print(my_sum(1, 2, 3, 4))
    print(my_sum(*[10, 20, 30, 40]))