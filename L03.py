from statistics import mean
import matplotlib.pyplot as plt

from L02 import (
    get_list_of_random_ints,
    get_bubble_sorted,
    get_insertion_sorted,
    get_selection_sorted,
    get_time_of_sort,
)

LENGTHS = [50, 100, 200, 500, 1000, 2000]


def measure_time_n_times(n, lst_length):
    res = {"bubble": [], "insertion": [], "selection": []}

    for _ in range(n):
        vector = get_list_of_random_ints(lst_length, min=0, max=5000)
        res["bubble"].append(get_time_of_sort(get_bubble_sorted, vector))
        res["insertion"].append(get_time_of_sort(get_insertion_sorted, vector))
        res["selection"].append(get_time_of_sort(get_selection_sorted, vector))

    return res


def plot_mean_time_of_every_sort_func(times_of_sort):

    bubble_mean = [mean(lst["bubble"]) for lst in times_of_sort]
    insertion_mean = [mean(lst["insertion"]) for lst in times_of_sort]
    selection_mean = [mean(lst["selection"]) for lst in times_of_sort]

    plt.plot(LENGTHS, bubble_mean, label="bubble sort")
    plt.plot(LENGTHS, insertion_mean, label="insertion sort")
    plt.plot(LENGTHS, selection_mean, label="selection sort")

    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title("Porównanie średniego czasu sortowania")

    plt.show()


def plot_stats_of_sort_func(sort_func_key: str, times_of_sort):

    max_time = [max(lst[sort_func_key]) for lst in times_of_sort]
    mean_time = [mean(lst[sort_func_key]) for lst in times_of_sort]
    min_time = [min(lst[sort_func_key]) for lst in times_of_sort]

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
    plot_stats_of_sort_func("bubble", times_of_sort)
    plot_stats_of_sort_func("insertion", times_of_sort)
    plot_stats_of_sort_func("selection", times_of_sort)
