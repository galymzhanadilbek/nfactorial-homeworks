def load_ascii_patterns(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    ascii_patterns = {}

    ascii_order = (
        " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    )
    char_height = 8

    for idx, char in enumerate(ascii_order):
        start_line = idx * (char_height + 1)
        if start_line + char_height <= len(lines):
            ascii_patterns[char] = [
                lines[start_line + i].rstrip("\n") for i in range(char_height)
            ]
        else:
            print(f"Warning: Missing pattern for character '{char}' due to insufficient lines.")

    return ascii_patterns


def generate_ascii_art(input_text, ascii_patterns):
    art_lines = [""] * 8

    for line in input_text.splitlines():
        for i in range(8):
            ascii_art_line = []
            for char in line:
                if char in ascii_patterns:
                    ascii_art_line.append(ascii_patterns[char][i])
                else:
                    ascii_art_line.append(" " * 8)
            art_lines[i] += " ".join(ascii_art_line) + "  "
        art_lines.append("")

    return "\n".join(art_lines)
