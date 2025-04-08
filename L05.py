import random

from BinaryTree import BinaryTree
from BinaryHeap import BinaryHeap

if __name__ == "__main__":

    # zad. 2
    vector = [random.randint(0, 10) for _ in range(10)]

    tree = BinaryTree(vector[0])
    for val in vector[1:]:
        tree.insert_node_simple(val)

    print("Wektor:", vector)
    print("\nStruktura drzewa:")
    print(tree)

    # zad. 4
    heap = BinaryHeap()
    for val in vector:
        heap.insert(val)

    print("Kopiec jako lista:", heap.heap)
    print("\nStruktura drzewa:")
    print(heap)
