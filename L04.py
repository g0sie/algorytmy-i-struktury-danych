from typing import List
import matplotlib.pyplot as plt
from statistics import mean

from L02 import get_list_of_random_ints, get_time_of_sort
from L04_sort import get_merge_sorted, get_counting_sorted, get_quick_sorted

LENGTHS = [50, 100, 200, 500, 1000, 2000]


def measure_time_n_times(n, lst_length):
    res = {"merge": [], "counting": [], "quick": []}

    for _ in range(n):
        vector = get_list_of_random_ints(lst_length, min=0, max=5000)
        res["merge"].append(get_time_of_sort(get_merge_sorted, vector))
        res["counting"].append(get_time_of_sort(get_counting_sorted, vector))
        res["quick"].append(get_time_of_sort(get_quick_sorted, vector))

    return res


def plot_mean_time_of_every_sort_func(times_of_sort):

    merge_mean = [mean(dict["merge"]) for dict in times_of_sort]
    counting_mean = [mean(dict["counting"]) for dict in times_of_sort]
    quick_mean = [mean(dict["quick"]) for dict in times_of_sort]

    plt.plot(LENGTHS, merge_mean, label="merge sort")
    plt.plot(LENGTHS, counting_mean, label="counting sort")
    plt.plot(LENGTHS, quick_mean, label="quick sort")

    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title("Porównanie średniego czasu sortowania")

    plt.show()


def plot_stats_of_sort_func(sort_func_key: str, times_of_sort):

    max_time = [max(dict[sort_func_key]) for dict in times_of_sort]
    mean_time = [mean(dict[sort_func_key]) for dict in times_of_sort]
    min_time = [min(dict[sort_func_key]) for dict in times_of_sort]

    plt.plot(LENGTHS, max_time, label="max")
    plt.plot(LENGTHS, mean_time, label="avg")
    plt.plot(LENGTHS, min_time, label="min")

    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title(f"Czas wykonanania {sort_func_key} sort")

    plt.show()


if __name__ == "__main__":

    times_of_sort = [measure_time_n_times(100, length) for length in LENGTHS]
    plot_mean_time_of_every_sort_func(times_of_sort)
    plot_stats_of_sort_func("merge", times_of_sort)
    plot_stats_of_sort_func("counting", times_of_sort)
    plot_stats_of_sort_func("quick", times_of_sort)
