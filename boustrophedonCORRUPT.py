
def boustrophedon_format(text, columns, corruption_side, tokens_to_corrupt, corrupt_every_line=False):
    lines = []
    reversed_lines = []

    # Split the text into lines of the specified column width
    for i in range(0, len(text), columns):
        line = text[i:i + columns]
        lines.append(line)

    # Reverse every other line
    for i, line in enumerate(lines):
        if i % 2 == 1:
            reversed_lines.append(line[::-1])
        else:
            reversed_lines.append(line)

    # Apply corruption based on user choice
    for i, line in enumerate(reversed_lines):
        if corrupt_every_line or i % 2 == 1:
            if corruption_side == "left":
                line = "X" * tokens_to_corrupt + line[tokens_to_corrupt:]
            elif corruption_side == "right":
                line = line[:-tokens_to_corrupt] + "X" * tokens_to_corrupt
            reversed_lines[i] = line

    return '\n'.join(reversed_lines)

def main():
    print("Boustrophedon Text Formatter")
    print("Enter the text you want to format:")
    input_text = input()

    print("Enter the number of columns (tokens per line):")
    columns = int(input())

    print("Enter the corruption side ('left' or 'right'):")
    corruption_side = input()

    print("Enter the number of tokens to corrupt:")
    tokens_to_corrupt = int(input())

    print("Corrupt every line? (yes/no):")
    corrupt_every_line_input = input().strip().lower()
    corrupt_every_line = corrupt_every_line_input == 'yes'

    formatted_text = boustrophedon_format(input_text, columns, corruption_side, tokens_to_corrupt, corrupt_every_line)
    
    print("\nFormatted Text:")
    print(formatted_text)

if __name__ == "__main__":
    main()
