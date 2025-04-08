from typing import List

from L05_BinaryHeap import BinaryHeap


def get_heap_sorted(lst: List[int]) -> List[int]:
    heap = BinaryHeap(lst)
    n = len(lst)

    sorted = [0 for _ in range(n)]

    # Wyciąganie największego elementu z kopca i umieszczanie go na końcu

    # iteracja po wszystkich elementach od ostatniego
    for i in range(n - 1, -1, -1):
        # zamiana korzenia (największego elementu) z ostatnim
        heap.heap[0], heap.heap[i] = heap.heap[i], heap.heap[0]
        # oderwanie i wrzucenie największego elementu na koniec listy
        sorted[i] = heap.heap.pop()
        # kopcowanie nowego korzenia w dół
        heap._heapify_down(0)

    return sorted
