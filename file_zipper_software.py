import heapq
from collections import Counter, namedtuple
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq_map = Counter(data)
    priority_queue = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(root, code='', mapping={}):
    if root is not None:
        if root.char is not None:
            mapping[root.char] = code
        generate_huffman_codes(root.left, code + '0', mapping)
        generate_huffman_codes(root.right, code + '1', mapping)
    return mapping

def compress_file(input_file, output_file, encoding_table):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encoded_data = ''.join(encoding_table.get(char, '') for char in data.decode('latin1'))

    # Convert binary string to bytes
    encoded_bytes = int(encoded_data, 2).to_bytes((len(encoded_data) + 7) // 8, byteorder='big')
    
    with open(output_file, 'wb') as f:
        f.write(encoded_bytes)

def decompress_file(input_file, output_file, root):
    with open(input_file, 'rb') as f:
        encoded_bytes = f.read()
    
    # Convert bytes to binary string
    encoded_data = bin(int.from_bytes(encoded_bytes, byteorder='big'))[2:]
    
    current_node = root
    decoded_data = ''
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root
    
    with open(output_file, 'w') as f:
        f.write(decoded_data)
        
def get_file_size(file_path):
    return os.path.getsize(file_path) / 1024

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input file path relative to the script directory
input_file = os.path.join(script_dir, 'input.txt')
output_file = os.path.join(script_dir, 'compressed.bin')

output_log_file = os.path.join(script_dir, 'output_log.txt')

# Read data from input file
with open(input_file, 'rb') as f:
    data = f.read().decode('utf-8') 

# Open output log file
with open(output_log_file, 'w') as log_file:
    # Print separator line to output log file
    print("----------------------------------------------------------------------------------------", file=log_file)
    print("Data read from input file:", data, file=log_file)
    print("----------------------------------------------------------------------------------------", file=log_file)
    # Print size of data before compression to output log file
    print("Size of data before compression:", get_file_size(input_file), "KB", file=log_file)

    # Build Huffman tree and generate Huffman codes
    huffman_tree = build_huffman_tree(data)
    encoding_table = generate_huffman_codes(huffman_tree)

    # Compress input file
    compress_file(input_file, output_file, encoding_table)
    print("-----------------------------------------------------------------------------------------", file=log_file)
    print("Compression complete", file=log_file)

    # Print size of compressed data to output log file
    print("Size of compressed data:", get_file_size(output_file), "KB", file=log_file)
