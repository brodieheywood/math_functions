# Brodie Heywood
# Dec, 2018

"""Ackermann's Function"""
# TODO: comment functions

import time


def ackermann(m, n):
    """

    PARAM:
    PRECONDITION:
    POSTCONDITION:
    RETURN:
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def pair_generator():
    """

    PARAM:
    PRECONDITION:
    POSTCONDITION:
    RETURN:
    """
    pairs = {}

    for x in range(6):
        for y in range(6):
            pairs[(x, y)] = []

    # list_of_keys = list(pairs.keys())
    # return list_of_keys
    return pairs


# def ackermann_loader(list):
#     start_time = time.perf_counter_ns()
#     for x in range(len(list) + 1):
#         ackermann(list[x][0], list[x][1])
#         end_time = time.perf_counter_ns()
#         print('Took %s nanoseconds to calculate.' % (end_time - start_time))

def ackermann_loader(dict):
    start_time_in_seconds = time.perf_counter_ns() * (10**-9)
    try:
        for key, value in dict.items():
            result = ackermann(key[0], key[1])
            end_time_in_seconds = time.perf_counter_ns() * (10**-9)
            dict[key] = [end_time_in_seconds - start_time_in_seconds, len(str(result)), result]
            print(dict)
    except RecursionError:
        print('No can do.')


# print(ackermann(pair_generator()[0][0], pair_generator()[0][1]))
ackermann_loader(pair_generator())
