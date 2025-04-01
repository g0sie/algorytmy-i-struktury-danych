from typing import List


def get_merge_sorted(lst: List[int]) -> List[int]:
    """Return a new list, sorted with merge sort."""

    def merge(left: List[int], right: List[int]) -> List[int]:
        """Merge two lists into one sorted."""
        result = []
        i, j = 0, 0

        # compare elements to find smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # if only one list left, insert all elements
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    if len(lst) <= 1:
        return lst

    n = len(lst) // 2
    left = lst[:n]
    right = lst[n:]
    return merge(get_merge_sorted(left), get_merge_sorted(right))


def get_counting_sorted(lst: List[int]) -> List[int]:
    """Return a new list, sorted with counting sort."""

    min_elem = min(lst)
    max_elem = max(lst)

    # count occurances of a number
    count_lst = [0 for _ in range(max_elem - min_elem + 1)]

    for elem in lst:
        count_lst[elem - min_elem] += 1

    # insert numbers in proper order
    result = []
    for i, count in enumerate(count_lst):
        for _ in range(count):
            result.append(i + min_elem)

    return result


def get_quick_sorted(lst: List[int]) -> List[int]:
    """Return a new list, sorted with quick sort."""

    def partition(lst: List[int], lo: int, hi: int) -> int:
        # segment - elementy pomiędzy indeksami lo i hi
        i = lo
        pivot = lst[hi]

        # szukamy elementów mniejszych od pivota
        # i ustawiamy jest na początku
        # swapując te mniejsze elementy z tymi początkowymi
        for j in range(lo, hi + 1):
            # jeżeli element jest mniejszy niż pivot
            # to swapnij go na początek
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1

        # wstaw pivota w odpowiednie miejsce
        # od lo do i-1 są mniejsze
        # od i+1 do hi są >=
        lst[i], lst[hi] = lst[hi], lst[i]

        # zwróć pozycję pivota
        return i

    def quick_sort_segment(lst: List[int], lo: int, hi: int):
        if lo >= hi:
            return

        # podziel listę tak, że
        # od lo do i-1: < pivot
        # i: pivot
        # od i+1 do hi: >= pivot
        i = partition(lst, lo, hi)
        quick_sort_segment(lst, lo, i - 1)
        quick_sort_segment(lst, i + 1, hi)

    lst = lst[:]
    quick_sort_segment(lst, 0, len(lst) - 1)
    return lst
