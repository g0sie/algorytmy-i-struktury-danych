import random
import matplotlib.pyplot as plt
from statistics import mean

from L02 import get_list_of_random_ints, get_time_of_sort
from L04_sort import get_merge_sorted, get_counting_sorted, get_quick_sorted
from L05_BinaryTree import BinaryTree
from L05_BinaryHeap import BinaryHeap
from L05_heap_sort import get_heap_sorted


LENGTHS = [50, 100, 200, 500, 1000, 2000]


def measure_time_n_times(n, lst_length):
    res = {"merge": [], "counting": [], "quick": [], "heap": []}

    for _ in range(n):
        vector = get_list_of_random_ints(lst_length, min=0, max=5000)
        res["merge"].append(get_time_of_sort(get_merge_sorted, vector))
        res["counting"].append(get_time_of_sort(get_counting_sorted, vector))
        res["quick"].append(get_time_of_sort(get_quick_sorted, vector))
        res["heap"].append(get_time_of_sort(get_heap_sorted, vector))

    return res


def plot_mean_time_of_every_sort_func(times_of_sort):

    merge_mean = [mean(dict["merge"]) for dict in times_of_sort]
    counting_mean = [mean(dict["counting"]) for dict in times_of_sort]
    quick_mean = [mean(dict["quick"]) for dict in times_of_sort]
    heap_mean = [mean(dict["heap"]) for dict in times_of_sort]

    plt.plot(LENGTHS, merge_mean, label="merge sort")
    plt.plot(LENGTHS, counting_mean, label="counting sort")
    plt.plot(LENGTHS, quick_mean, label="quick sort")
    plt.plot(LENGTHS, heap_mean, label="heap sort")

    plt.legend()
    plt.grid()

    plt.xlabel("długość listy")
    plt.ylabel("czas sortowania [ns]")
    plt.title("Porównanie średniego czasu sortowania")

    plt.show()


if __name__ == "__main__":

    # zad. 2
    vector = [random.randint(0, 10) for _ in range(10)]

    tree = BinaryTree(vector[0])
    for val in vector[1:]:
        tree.insert_node_simple(val)

    print("Wektor:", vector)
    print("Struktura drzewa:")
    print(tree)

    # zad. 4
    heap = BinaryHeap(vector)

    print("Kopiec jako lista:", heap.heap)
    print("Struktura drzewa:")
    print(heap)

    # zad. 5
    sorted = get_heap_sorted(vector)
    print(sorted)

    # zad. 6 - złożoność heap sorta
    # budowanie kopca: O(n)
    # wyciąganie elementów: O(n log n),
    # bo heapify_down ma O(log n)

    # zad. 7
    times_of_sort = [measure_time_n_times(100, length) for length in LENGTHS]
    plot_mean_time_of_every_sort_func(times_of_sort)
