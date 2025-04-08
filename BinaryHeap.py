class BinaryHeap:
    def __init__(self):
        self.heap = []
        # rodzic w i -> dzieci w 2i+1, 21+2
        # dziecko w i -> rodzic w (i-2)//2

    def insert(self, value):
        # dodaj element na koniec i wyciągnij go do góry
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # metoda ważna przy dodawaniu elementów
    # wyciąganie większego elementu do góry
    def _heapify_up(self, index):
        # indeks rodzica dodanego elementu
        parent = (index - 1) // 2

        # jeżeli nasz element:
        # - nie jest korzeniem
        # - jego wartość jest większa niż rodzica
        if index > 0 and self.heap[index] > self.heap[parent]:
            # zamieniami wartość elementu i wartość rodzica
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # robimy heapify na rodzicu
            self._heapify_up(parent)

    # usuń i zwróć korzeń - największy element
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # przenosimy ostatni element na górę
        self.heap[0] = self.heap.pop()

        # ściągamy do w dół w odpowiednie miejsce
        self._heapify_down(0)
        return root

    # metoda ważna przy usuwaniu elementów
    # ściąganie elementu w dół
    def _heapify_down(self, index):
        left = 2 * index + 1  # indeks lewego dziecka
        right = 2 * index + 2  # indeks prawego dziecka
        largest = index  # indeks elementu, który ściągamy w dół

        # jeżeli któreś dziecko ma większą wartość niż nasz element
        # largest = indeks dziecka
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # dziecko było większe ->
        if largest != index:
            # swapujemy nasz element i to dziecko
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # ściągamy ten element dalej w dół
            self._heapify_down(largest)

    def _str_helper(self, index=0, prefix="", is_left=True):
        result = prefix
        result += "├── " if is_left else "└── "
        result += str(self.heap[index]) + "\n"

        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap):
            result += self._str_helper(
                left, prefix + ("│   " if is_left else "    "), True
            )

        if right < len(self.heap):
            result += self._str_helper(
                right, prefix + ("│   " if is_left else "    "), False
            )

        return result

    def __str__(self):
        return self._str_helper()
