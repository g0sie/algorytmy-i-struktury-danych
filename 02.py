import random as rnd
import time as tm

import matplotlib.pyplot as plt
import tabulate as tbl
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


def get_time_of_sort(sort_func: Callable[[List[int]], List[int]], vector: List[int]):
    start = tm.perf_counter_ns()
    sort_func(vector)
    stop = tm.perf_counter_ns()
    return stop - start


def print_times_of_sort(
    lengths, times_of_bubble_sort, times_of_insertion_sort, times_of_selection_sort
):
    data = [
        [
            lengths[i],
            times_of_bubble_sort[i],
            times_of_insertion_sort[i],
            times_of_selection_sort[i],
        ]
        for i in range(len(lengths))
    ]
    headers = ["length", "bubble", "insertion", "selection"]
    print(tbl.tabulate(data, headers=headers))


def plot_times_of_sort(
    lengths, times_of_bubble_sort, times_of_insertion_sort, times_of_selection_sort
):
    plt.plot(lengths, times_of_bubble_sort, label="bąbelkowe")
    plt.plot(lengths, times_of_insertion_sort, label="przez wstawianie")
    plt.plot(lengths, times_of_selection_sort, label="przez wybieranie")
    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title("Porównanie czasu sortowania algorytmów")

    plt.show()


if __name__ == "__main__":

    lengths = [50, 100, 200, 500, 1000, 2000]

    # generate vectors to sort
    vectors = [get_list_of_random_ints(n=length, min=0, max=5000) for length in lengths]

    # get times of sort functions
    times_of_bubble_sort = [
        get_time_of_sort(get_bubble_sorted, vector) for vector in vectors
    ]
    times_of_insertion_sort = [
        get_time_of_sort(get_insertion_sorted, vector) for vector in vectors
    ]
    times_of_selection_sort = [
        get_time_of_sort(get_selection_sorted, vector) for vector in vectors
    ]

    print_times_of_sort(
        lengths, times_of_bubble_sort, times_of_insertion_sort, times_of_selection_sort
    )

    plot_times_of_sort(
        lengths, times_of_bubble_sort, times_of_insertion_sort, times_of_selection_sort
    )
