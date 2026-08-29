import heapq


class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def build_huffman_tree(characters, frequencies):
    heap = []

    for i in range(len(characters)):
        node = Node(characters[i], frequencies[i])
        heapq.heappush(heap, (frequencies[i], i, node))

    count = len(characters)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        parent = Node(None, f1 + f2)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, (f1 + f2, count, parent))
        count += 1

    return heap[0][2]


def decode_huffman(characters, frequencies, encoded_string):
    root = build_huffman_tree(characters, frequencies)

    result = []
    current = root

    for bit in encoded_string:

        if bit == '0':
            current = current.left
        else:
            current = current.right

        # Reached a character
        if current.char is not None:
            result.append(current.char)
            current = root

    return ''.join(result)


# Test Case 1
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]

encoded_string = '1101100111110'

print("Decoded message:",
      decode_huffman(
          characters,
          frequencies,
          encoded_string
      ))


# Test Case 2
characters = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies = [5, 9, 12, 13, 16, 45]

encoded_string = '110011011100101111001011'

print("Decoded message:",
      decode_huffman(
          characters,
          frequencies,
          encoded_string
      ))
