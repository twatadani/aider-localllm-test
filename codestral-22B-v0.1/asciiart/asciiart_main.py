import sys
from art import text2art

def convert_to_ascii(text):
    """Convert input text to ASCII art.

    Args:
        text (str): The text to convert.

    Returns:
        str: The ASCII art representation of the text.
    """
    return text2art(text)

if __name__ == '__main__':
    # Get the input text from command line arguments.
    input_text = ' '.join(sys.argv[1:])

    # Convert the input text to ASCII art and print it.
    ascii_art = convert_to_ascii(input_text)
    print(ascii_art)
