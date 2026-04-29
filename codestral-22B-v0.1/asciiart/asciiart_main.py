import sys
from shutil import get_terminal_size

def convert_to_ascii(text):
    """Convert input text to ASCII art.

    Args:
        text (str): The text to convert.

    Returns:
        str: The ASCII art representation of the text.
    """
    # Get terminal width to center the ASCII art.
    terminal_width = get_terminal_size().columns

    # Create a list of ASCII characters to use for the art.
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    # Convert the input text to ASCII art.
    ascii_art = ''
    for char in text:
        # Map each character to an ASCII art representation.
        ascii_char = ascii_chars[ord(char) % len(ascii_chars)]
        # Center the ASCII art by adding padding.
        padding = ' ' * ((terminal_width - len(text)) // 2)
        ascii_art += padding + ascii_char * len(text) + '\n'
    return ascii_art

if __name__ == '__main__':
    # Get the input text from command line arguments.
    input_text = ' '.join(sys.argv[1:])

    # Convert the input text to ASCII art and print it.
    ascii_art = convert_to_ascii(input_text)
    print(ascii_art)
