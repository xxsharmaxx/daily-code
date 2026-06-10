letters = {
    'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCCC', 'C    ', 'C    ', 'C    ', ' CCCC'],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
    'G': [' GGGG', 'G    ', 'G GGG', 'G   G', ' GGG '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
    'J': ['JJJJJ', '   J ', '   J ', 'J  J ', ' JJ  ']
}

def print_ascii(text):
    text = text.upper()

    for row in range(5):
        line = ""

        for char in text:
            if char in letters:
                line += letters[char][row] + "  "
            else:
                line += "     "

        print(line)

while True:
    text = input("\nEnter text (or exit): ")

    if text.lower() == "exit":
        break

    print("\n")
    print_ascii(text)
