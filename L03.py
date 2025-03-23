from statistics import mean
import matplotlib.pyplot as plt

from L02 import (
    get_list_of_random_ints,
    get_bubble_sorted,
    get_insertion_sorted,
    get_selection_sorted,
    get_time_of_sort,
)


def measure_time_n_times(n, lst_length):
    res = {"bubble": [], "insertion": [], "selection": []}

    for _ in range(n):
        vector = get_list_of_random_ints(lst_length, min=0, max=5000)
        res["bubble"].append(get_time_of_sort(get_bubble_sorted, vector))
        res["insertion"].append(get_time_of_sort(get_insertion_sorted, vector))
        res["selection"].append(get_time_of_sort(get_selection_sorted, vector))

    return res


def plot_mean_time_of_every_sort_func(lengths, times_of_sort):

    bubble_mean = [mean(lst["bubble"]) for lst in times_of_sort]
    insertion_mean = [mean(lst["insertion"]) for lst in times_of_sort]
    selection_mean = [mean(lst["selection"]) for lst in times_of_sort]

    plt.plot(lengths, bubble_mean, label="bubble sort")
    plt.plot(lengths, insertion_mean, label="insertion sort")
    plt.plot(lengths, selection_mean, label="selection sort")

    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title("Porównanie średniego czasu sortowania")

    plt.show()


if __name__ == "__main__":

    lengths = [50, 100, 200, 500, 1000, 2000]
    times_of_sort = [measure_time_n_times(10, length) for length in lengths]
    plot_mean_time_of_every_sort_func(lengths, times_of_sort)
