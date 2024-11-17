import sys
from ascii_generator import load_ascii_patterns, generate_ascii_art

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 src/main.py <text> <font>")
        return

    input_text = sys.argv[1].encode().decode("unicode_escape")
    font = sys.argv[2]

    font_file = f"src/{font}.txt"

    try:
        ascii_patterns = load_ascii_patterns(font_file)
    except FileNotFoundError:
        print(f"Error: Font file '{font_file}' not found.")
        return

    ascii_art = generate_ascii_art(input_text, ascii_patterns)
    print("Generated ASCII Art:")
    print(ascii_art)

if __name__ == "__main__":
    main()
