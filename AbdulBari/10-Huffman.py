import heapq

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(chars, freq):
    # Create a priority queue of nodes
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

def calculate_total_compression(chars, freq, codes):
    total_bits = sum(len(codes[char]) * frequency for char, frequency in zip(chars, freq))
    return total_bits

# Given example
chars = ['a', 'b', 'c', 'd', 'e']
freq = [3, 5, 6, 4, 2]

# Build the Huffman tree
root = build_huffman_tree(chars, freq)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

# Print Huffman codes
print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")

# Calculate and print total compression
total_compression = calculate_total_compression(chars, freq, huffman_codes)
print(f"Total compression (bits): {total_compression}")
