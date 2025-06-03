import heapq
import time
from collections import Counter
from tabulate import tabulate
import matplotlib.pyplot as plt


# Klasa reprezentująca węzeł drzewa Huffmana
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char  # znak
        self.freq = freq  # liczba wystąpień
        self.left = None  # lewe dziecko
        self.right = None  # prawe dziecko

    def __lt__(self, other):  # less than <
        return self.freq < other.freq


# Budowanie drzewa Huffmana na podstawie tekstu
def build_tree(text):
    freq = Counter(text)  # zliczanie wystąpień znaków
    heap = [Node(c, f) for c, f in freq.items()]
    heapq.heapify(
        heap
    )  # zamiana listy na kopiec, dzięki temu najmniejsza wartość (czyli najrzadszy znak) jest na górze

    while len(heap) > 1:  # łączymy węzły w pary aż zostanie tylko jeden węzeł
        # bierzemy dwa węzły z najmniejszą liczbą wystąpień
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # łączymy w jeden
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)  # dodanie nowego węzła do kopca

    return heap[0]  # korzeń drzewa


# Generowanie kodów Huffmana na podstawie drzewa
def generate_codes(node, prefix="", codebook={}):
    if node is None:
        return codebook

    # jeżeli znak(liść) to dodajemy kod do słownika
    if node.char is not None:
        codebook[node.char] = prefix

    # idziemy w lewo -> dodajemy 0 do kodu
    # idziemy w prawo -> dodajemy 1 do kodu
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)
    return codebook


# Kodowanie tekstu za pomocą kodów Huffmana
def encode(text, codebook):
    # zamieniamy każdy znak na kod
    return "".join(codebook[c] for c in text)


# Dekodowanie zakodowanego ciągu bitów
def decode(encoded, tree):
    decoded = ""
    node = tree
    # sprawdzamy bity i idziemy lewo albo prawo aż dojdziemy do znaku (liścia)
    # zapisujemy znak i wracamy do korzenia
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded += node.char
            node = tree  # powrót do korzenia
    return decoded


# Obliczanie liczby bitów przed i po kompresji
def bit_counts(text, encoded):
    return len(text) * 8, len(encoded)  # zakładamy 8 bitów na znak oryginalny


# Obliczanie współczynnika kompresji
def compression_ratio(original, compressed):
    return (compressed / original) * 100


# Analiza tekstu – budowa drzewa, kompresja, dekompresja i wyniki
def analyze_text(text):
    tree = build_tree(text)
    codebook = generate_codes(tree)
    encoded = encode(text, codebook)
    decoded = decode(encoded, tree)

    headers = ["Znak", "Liczba wystąpień", "Kod Huffmana"]
    table = [(f"'{c}'", text.count(c), codebook[c]) for c in sorted(codebook)]
    print(tabulate(table, headers=headers, tablefmt="grid"))

    original_bits, compressed_bits = bit_counts(text, encoded)
    print(f"\nZakodowany ciąg binarny: {encoded}")
    print(f"\nOdkodowany tekst: {decoded}")
    print(
        f"\nBity przed kompresją: {original_bits}, Bity po kompresji: {compressed_bits}"
    )
    print(
        f"Współczynnik kompresji: {compression_ratio(original_bits, compressed_bits):.2f}%"
    )
    return original_bits, compressed_bits, len(text), len(encoded), tree


# Wydajnościowa analiza wielu plików tekstowych
def benchmark(files):
    original_sizes = []
    compressed_sizes = []
    comp_times = []
    decomp_times = []
    compression_levels = []

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        # kompresja
        start = time.time()
        tree = build_tree(text)
        codebook = generate_codes(tree)
        encoded = encode(text, codebook)
        comp_time = time.time() - start

        # dekompresja
        start = time.time()
        decode(encoded, tree)
        decomp_time = time.time() - start

        # liczba bitów
        original_bits, compressed_bits = bit_counts(text, encoded)

        # poziom kompresji
        ratio = compression_ratio(original_bits, compressed_bits)

        original_sizes.append(len(text))
        compressed_sizes.append(compressed_bits)
        comp_times.append(comp_time)
        decomp_times.append(decomp_time)
        compression_levels.append(ratio)

    # Wykres: liczba bitów przed i po kompresji
    plt.plot(original_sizes, [s * 8 for s in original_sizes], label="Przed kompresją")
    plt.plot(original_sizes, compressed_sizes, label="Po kompresji")
    plt.xlabel("Liczba znaków")
    plt.ylabel("Liczba bitów")
    plt.title("Liczba bitów przed i po kompresji")
    plt.legend()
    plt.show()

    # Wykres: czas kompresji i dekompresji
    plt.plot(original_sizes, comp_times, label="Czas kompresji")
    plt.plot(original_sizes, decomp_times, label="Czas dekompresji")
    plt.xlabel("Liczba znaków")
    plt.ylabel("Czas (s)")
    plt.title("Czas kompresji i dekompresji")
    plt.legend()
    plt.show()

    # Wykres: poziom kompresji
    plt.plot(original_sizes, compression_levels)
    plt.xlabel("Liczba znaków")
    plt.ylabel("Poziom kompresji (%)")
    plt.title("Poziom kompresji")
    plt.show()


if __name__ == "__main__":
    # analyze_text("Lorem ipsum dolor sit amet.")
    benchmark(
        ["1_wers.txt", "3_wersy.txt", "10_wersow.txt", "25_wersow.txt", "50_wersow.txt"]
    )
