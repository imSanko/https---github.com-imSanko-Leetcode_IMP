
    "111110010001010010010010111110010001": "Z",
    "111110010001010010010010010010010010": "X"
}

def extract_letter(grid):
    letter_pattern = ''.join(''.join(row) for row in grid)
    return alphabet_patterns.get(letter_pattern, "?")

def split_input_grid(lines):
    cols = len(lines[0])
    letters = []
    start = 0

    while start < cols:
        if all(line[start] == '0' for line in lines):
            start += 1