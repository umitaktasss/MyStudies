import re
from graphviz import Digraph

# Token specification
token_specification = [
    ('KEYWORD',    r'\b(if|else|while|for|int|float)\b'),
    ('OPERATOR',   r'[+\-*/%<>=!&|]+'),
    ('FLOAT',      r'\b\d+\.\d+\b'),
    ('INTEGER',    r'\b\d+\b'),
    ('VARIABLE',   r'\b[a-z_][a-z0-9_]*\b'),
    ('PUNCTUATION', r'[;(){}]'),  # Added punctuation symbols
    ('SKIP',       r'[ \t\n]+'),
    ('MISMATCH',   r'.'),
]

def tokenize(code):
    tokens = []
    for tok in re.finditer('|'.join('(?P<%s>%s)' % pair for pair in token_specification), code):
        kind = tok.lastgroup
        value = tok.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
        tokens.append({'type': kind, 'value': value})
    return tokens

# Define Node class and functions to parse and visualize the parse tree
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def parse_expression(tokens):
    root = Node("Expression")
    for token in tokens:
        # Replace spaces with underscores in node names
        node_name = f"{token['type']}_{token['value']}"
        root.add_child(Node(node_name))
    return root

def visualize_tree(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()

    graph.node(node.name)
    if parent:
        graph.edge(parent.name, node.name)
    
    for child in node.children:
        visualize_tree(child, graph, node)
    
    return graph

# Example usage
code = "x = 5 + 3.14; if (x > 10) { y = 2.0 * x; }"
tokens = tokenize(code)
print(tokens)  # This will print the list of tokens for verification
parse_tree = parse_expression(tokens)
graph = visualize_tree(parse_tree)

# Save as .dot file
dot_filename = 'parse_tree.dot'
graph.save(dot_filename)

# Now use the dot command to convert .dot to .png with higher resolution
import os
png_filename = 'parse_tree.png'
os.system(f'dot -Tpng -Gdpi=300 {dot_filename} -o {png_filename}')

# Print the current working directory to find the file location
print(f"PNG file created at: {os.getcwd()}\\{png_filename}")
