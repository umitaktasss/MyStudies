import re

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

# Example usage
code = "x = 5 + 3.14; if (x > 10) { y = 2.0 * x; }"
tokens = tokenize(code)
for token in tokens:
    print(token)

