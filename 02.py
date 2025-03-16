import random as rnd
import time as tm

# import matplotlib.pyplot as plt
# import tabulate as tbl
from typing import List, Callable


def get_list_of_random_ints(n: int, min: int, max: int) -> List[int]:
    return [rnd.randint(min, max) for _ in range(n)]


def get_bubble_sorted(lst: List[int]) -> List[int]:
    lst = lst[:]
    n = len(lst)

    for i in range(n):
        for j in range(n - i - 1):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def get_insertion_sorted(lst: List[int]) -> List[int]:
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

    return lst


def get_selection_sorted(lst: List[int]) -> List[int]:
    lst = lst[:]

    for i in range(len(lst) - 1):
        min_idx = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst


def get_time_of_sort(
    sort_func: Callable[[List[int]], List[int]], vectors: List[List[int]]
):
    times = []

    for vector in vectors:
        start = tm.perf_counter_ns()
        sort_func(vector)
        stop = tm.perf_counter_ns()
        times.append(stop - start)

    return times


if __name__ == "__main__":
    # lst = get_list_of_random_ints(n=5, min=0, max=10)
    # print(lst)
    # print(get_bubble_sorted(lst))
    # print(get_insertion_sorted(lst))
    # print(get_selection_sorted(lst))
    # print(lst)

    lengths = [50, 100, 200, 500, 1000, 2000]

    vectors = [get_list_of_random_ints(n=length, min=0, max=5000) for length in lengths]

    print([len(vector) for vector in vectors])
    print(get_time_of_sort(sort_func=get_bubble_sorted, vectors=vectors))
    print(get_time_of_sort(sort_func=get_insertion_sorted, vectors=vectors))
    print(get_time_of_sort(sort_func=get_selection_sorted, vectors=vectors))
