import timeit
import numpy

"""
Part 1 of the performance python course
"""

times = 100_000_000


def for_loop():
    total = 0
    for i in range(times):
        total += i
    return total


def while_loop():
    my_list = []
    i = 0
    while i < times:
        my_list.append(i)
        i += 1


def sum_range():
    return sum(range(times))


def sum_range_numpy():
    return numpy.sum(numpy.arange(times))


def sum_math():
    return (times * (times - 1)) // 2


# create a function that takes two numbers and prints who how many percent faster the first number is compared to the second number
def percentage_difference(first, second):
    return ((first - second) / first) * 100 + "%"


def main():
    for_looped = timeit.timeit(for_loop, number=1)
    while_looped = timeit.timeit(while_loop, number=1)
    sum_ranged = timeit.timeit(sum_range, number=1)
    sum_ranged_numpy = timeit.timeit(sum_range_numpy, number=1)
    sum_mathed = timeit.timeit(sum_math, number=1)

    print(f'{"For loop":<10} {for_looped:.3f} {"seconds":<8}')
    print(f'{"While loop":<10} {while_looped:.3f} {"seconds":<8}')

    # print the difference between the two loops
    print(f'{"Difference":<10} {while_looped - for_looped:.3f} {"seconds":<8}')

    # print how much faster is the for loop compared to the while loop
    print(f'{"For loop is":<10} {for_looped / while_looped:.3f} {"times faster":<8}')
    # how many percent faster is the for loop compared to the while loop
    print(f'{"For loop is":<10} {for_looped / while_looped * 100:.3f} {"percent faster":<8}')

    # print the sum of the range
    print(f'{"Sum of range":<10} {sum_ranged}')

    # print the difference between the while loop and the sum of the range
    print(f'{"Difference":<10} {while_looped - sum_ranged:.3f} {"seconds":<8}')

    # print the percentage difference between the while loop and the sum of the range
    print(f'{"Percentage difference":<10} {((while_looped - sum_ranged) / while_looped) * 100:.3f} {"%":<8}')

    # print the difference between the for loop and the sum of the range
    print(f'{"Difference":<10} {for_looped - sum_ranged:.3f} {"seconds":<8}')

    # print the percentage difference between the for loop and the sum of the range
    print(f'{"Percentage difference":<10} {((for_looped - sum_ranged) / for_looped) * 100:.3f} {"%":<8}')

    # print the difference between the sum of the range and the sum of the range using numpy
    print(f'{"Difference":<10} {sum_ranged - sum_ranged_numpy:.3f} {"seconds":<8}')

    # print the percentage difference between the sum of the range and the sum of the range using numpy
    print(f'{"Percentage difference":<10} {((sum_ranged - sum_ranged_numpy) / sum_ranged) * 100:.3f} {"%":<8}')

    # how many times faster is the sum of the range using numpy than the sum of the range?
    print(f'{"Times faster":<10} {sum_ranged / sum_ranged_numpy:.3f} {"times":<8}')

    # print the difference between the sum of the range using numpy and the sum of the range using math
    print(f'{"Difference":<10} {sum_ranged_numpy - sum_mathed:.3f} {"seconds":<8}')

    # print the percentage difference between the sum of the range using numpy and the sum of the range using math
    print(f'{"Percentage difference":<10} {((sum_ranged_numpy - sum_mathed) / sum_ranged_numpy) * 100:.3f} {"%":<8}')

    # how many times faster is the sum of the range using math than the sum of the range using numpy?
    print(f'{"Times faster":<10} {sum_ranged_numpy / sum_mathed:.3f} {"times":<8}')


if __name__ == '__main__':
    main()
