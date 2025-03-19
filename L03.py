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


if __name__ == "__main__":

    lengths = [50, 100, 200, 500, 1000, 2000]
    times_of_sort = [measure_time_n_times(10, length) for length in lengths]
