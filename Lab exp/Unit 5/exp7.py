import heapq


class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def huffman_codes(characters, frequencies):
    heap = []

    # Add nodes to min heap
    for i in range(len(characters)):
        node = HuffmanNode(characters[i], frequencies[i])

        # Character used for deterministic tie-breaking
        heapq.heappush(heap, (frequencies[i], i, node))

    count = len(characters)

    # Build Huffman Tree
    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = HuffmanNode(
            None,
            freq1 + freq2
        )

        parent.left = left
        parent.right = right

        heapq.heappush(heap, (parent.freq, count, parent))
        count += 1

    root = heap[0][2]

    codes = {}

    def generate_codes(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")

    return sorted(codes.items())


# Test Case 1
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]

print("Huffman Codes:")
print(huffman_codes(characters, frequencies))


# Test Case 2
characters = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies = [5, 9, 12, 13, 16, 45]

print("Huffman Codes:")
print(huffman_codes(characters, frequencies))
