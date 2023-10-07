import heapq
import collections
import pickle

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, current_code, codes):
    if node.char is not None:
        codes[node.char] = current_code
    if node.left:
        build_huffman_codes(node.left, current_code + '0', codes)
    if node.right:
        build_huffman_codes(node.right, current_code + '1', codes)

def compress(input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()

    freq_dict = collections.Counter(data)
    root = build_huffman_tree(freq_dict)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    compressed_data = []
    for char in data:
        compressed_data.append(huffman_codes[char])

    with open(output_file, 'wb') as file:
        pickle.dump((root, compressed_data), file)

def decompress(input_file, output_file):
    with open(input_file, 'rb') as file:
        root, compressed_data = pickle.load(file)

    decompressed_data = []
    current_node = root

    for bit in compressed_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_data.append(current_node.char)
            current_node = root

    decompressed_data = bytes(decompressed_data)

    with open(output_file, 'wb') as file:
        file.write(decompressed_data)

# Пример использования:
input_file = 'input.txt'
output_file = 'compressed.huffman'
compress(input_file, output_file)
decompressed_file = 'decompressed.txt'
decompress(output_file, decompressed_file)

