import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

LENGTHS = [50, 100, 500, 1000, 2000]


# --------- BST -----------------------------------------
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_bst(root, val):
    # funkcja rekurencyjna, w zależności od wartości wstawiamy węzeł po lewej albo po prawej
    if root is None:
        return BST(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    return root


def search_bst(root, val):
    # szukamy węzła po lewej albo po prawej w zależności od wartości
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)


def get_min_bst(root):
    # minimum jest na dole po lewej
    while root.left:
        root = root.left
    return root


def get_max_bst(root):
    # maksimum jest na dole po prawej
    while root.right:
        root = root.right
    return root


def get_successor_bst(root, val):
    node = search_bst(root, val)

    # istnieje prawe poddrzewo -> szukamy tam najmniejszego
    if node.right:
        return get_min_bst(node.right)

    # nie istnieje -> szukamy najniższego przodka
    succ = None
    while root:
        if val < root.val:
            succ = root
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            break
    return succ


def get_predecessor_bst(root, val):
    node = search_bst(root, val)

    # istnieje lewe poddrzewo -> szukamy tam największego
    if node.left:
        return get_max_bst(node.left)
    pred = None

    # nie istnieje -> szukamy najniższego przodka, który jest mniejszy
    while root:
        if val > root.val:
            pred = root
            root = root.right
        elif val < root.val:
            root = root.left
        else:
            break
    return pred


def delete_bst(root, val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # liść -> ustawiamy None
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # znajdujemy następnika, kopiujemy klucz następnika, usuwamy następnika
        temp = get_min_bst(root.right)
        root.val = temp.val
        root.right = delete_bst(root.right, temp.val)
    return root


def inorder(root):
    # printowanie od lewej do prawej
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# --------- AVL -----------------------------------------


class AVL:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):  # -1, 0, 1
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(y):
    # rotacja prawa dla y
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2

    # update wysokości
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    # teraz x  jest korzeniem
    return x


def left_rotate(x):
    # rotacja lewa dla x
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2

    # update wysokości
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    # teraz y jest korzeniem
    return y


def insert_avl(root, val):
    # wstawiamy tak jak w BST, w zależności od wartości na lewo albo prawo
    if not root:
        return AVL(val)
    if val < root.val:
        root.left = insert_avl(root.left, val)
    elif val > root.val:
        root.right = insert_avl(root.right, val)
    else:
        return root

    # aktualizacja wysokości i wyważenia
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # jeżeli balans jest 0, -1, 1 -> jest ok
    # jeżeli balans jest 2 lub -2 -> trzeba wykonać rotacje

    # LL
    # nowy węzeł poszedł w lewo od lewego dziecka
    if balance > 1 and val < root.left.val:
        return right_rotate(root)
    # RR
    # nowy węzeł poszedł w prawo od prawego dziecka
    if balance < -1 and val > root.right.val:
        return left_rotate(root)
    # LR
    # nowy węzeł poszedł w prawo od lewego dziecka
    if balance > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RL
    # nowy węzeł poszedł w lewo od prawego dziecka
    if balance < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def min_value_node(node):
    # węzeł max na lewo
    current = node
    while current.left:
        current = current.left
    return current


def delete_avl(root, val):
    # usuwamy jak w BST
    if not root:
        return root
    if val < root.val:
        root.left = delete_avl(root.left, val)
    elif val > root.val:
        root.right = delete_avl(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete_avl(root.right, temp.val)

    # updatujemy wysokości i balans
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # robimy rotacje
    # LL
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    # LR
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RR
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    # RL
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def search_avl(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_avl(root.left, val)
    return search_avl(root.right, val)


def get_min_avl(root):
    return min_value_node(root)


def get_max_avl(root):
    # max na prawo
    current = root
    while current.right:
        current = current.right
    return current


# --------- zad 3 ------------------------------------


def get_vector_1_to(n):
    vector = [i for i in range(1, n + 1)]
    random.shuffle(vector)
    return vector


def insert_vector(vector):
    bst_root = None
    avl_root = None

    for val in vector:
        bst_root = insert_bst(bst_root, val)
        avl_root = insert_avl(avl_root, val)

    return {"bst": bst_root, "avl": avl_root}


# ----------- zad 4 ------------------------------


def measure_search_time(tree_root, search_func, search_values):
    start_time = time.perf_counter()
    for val in search_values:
        search_func(tree_root, val)
    end_time = time.perf_counter()
    return end_time - start_time


def measure_5_random_searches(trees, n):
    search_values = random.sample(range(1, n + 1), 5)
    times = []
    for value in search_values:
        bst_time = measure_search_time(trees["bst"], search_bst, search_values)
        avl_time = measure_search_time(trees["avl"], search_avl, search_values)
        times.append([value, bst_time, avl_time])
    headers = ["Value", "BST time", "AVL time"]
    print(tabulate(times, headers=headers, tablefmt="pretty"))


# --------------- zad 5, 6 ------------------------
def measure_many_lengths():
    results = {"bst": [], "avl": []}
    for length in LENGTHS:
        bst_total, avl_total = 0.0, 0.0
        for _ in range(100):  # Monte Carlo 100 powtórzeń
            vec = get_vector_1_to(length)
            trees = insert_vector(vec)
            search_values = random.choices(range(1, length + 1), k=100)
            bst_time = measure_search_time(trees["bst"], search_bst, search_values)
            avl_time = measure_search_time(trees["avl"], search_avl, search_values)
            bst_total += bst_time
            avl_total += avl_time
        results["bst"].append(bst_total / 100)
        results["avl"].append(avl_total / 100)
    return results


# ------------------- zad 7 ------------------------------
def plot(results):
    plt.figure(figsize=(10, 6))
    plt.plot(LENGTHS, results["bst"], label="BST", marker="o")
    plt.plot(LENGTHS, results["avl"], label="AVL", marker="o")
    plt.xlabel("Length of vector")
    plt.ylabel("Average search time (s)")
    plt.title("Search time vs. vector length")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    # zad 1 - bst
    root = None
    for val in [10, 5, 15, 3, 7, 12, 18]:
        root = insert_bst(root, val)

    print("Inorder:")
    inorder(root)  # powinno wypisać: 3 5 7 10 12 15 18

    print("\nMin:", get_min_bst(root).val)
    print("Max:", get_max_bst(root).val)
    print("Search 7:", search_bst(root, 7) is not None)
    print("Successor 10:", get_successor_bst(root, 10).val)
    print("Predecessor 10:", get_predecessor_bst(root, 10).val)

    root = delete_bst(root, 10)
    print("Inorder after deleting 10:")
    inorder(root)  # powinno wypisać: 3 5 7 12 15 18

    # zad 2 - avl
    root = None
    for val in [10, 20, 30, 40, 50, 25]:
        root = insert_avl(root, val)

    print("Inorder:")
    inorder(root)  # powinno wypisać w kolejności rosnącej

    print("\nMin:", get_min_avl(root).val)
    print("Max:", get_max_avl(root).val)
    print("Search 30:", search_avl(root, 30) is not None)

    root = delete_avl(root, 40)
    print("Inorder after deleting 40:")
    inorder(root)

    # zad 3
    vec15 = get_vector_1_to(15)
    trees15 = insert_vector(vec15)
    print("\n[1-15]: ", vec15)
    print("\nBST inorder:")
    inorder(trees15["bst"])

    print("\nAVL inorder:")
    inorder(trees15["avl"])

    # zad 4
    measure_5_random_searches(trees15, 15)

    # zad 5 + 6
    results = measure_many_lengths()
    print(results)

    # zad 7
    plot(results)
