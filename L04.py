from typing import List
from L02 import get_list_of_random_ints


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

    # TODO: make better version of this algorithm XD
    # message for later: kocham cię Gosia <3

    if len(lst) <= 1:
        return lst

    pivot = lst[-1]

    less = [elem for elem in lst[:-1] if elem <= pivot]
    greater = [elem for elem in lst[:-1] if elem > pivot]

    return get_quick_sorted(less) + [pivot] + get_quick_sorted(greater)


if __name__ == "__main__":
    # vec = get_list_of_random_ints(n=5, min=0, max=9)
    vec = [1, 5, 7, 2, 2, 3]
    # print(vec)
    print("start: ", vec)
    sorted = get_counting_sorted(vec)
    print("result: ", sorted)
