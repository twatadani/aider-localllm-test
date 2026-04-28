# Main entry point for the ASCII art generator

import sys
from asciiart.asciiart import generate_ascii_art, invert_string

def main():
    """
    Main function to handle command line arguments and generate ASCII art.
    
    This function reads the command line arguments, processes them, and generates
    ASCII art based on the input text. It also inverts the string if needed.
    """
    # Check if at least one argument is provided
    if len(sys.argv) < 2:
        print("Usage: python asciiart_main.py [text] [options]")
        print("Options:")
        print("  -i, --invert: Invert the input string")
        print("  -w, --width=WIDTH: Set the width of the ASCII art (default is 80)")
        sys.exit(1)

    # Extract the text from the command line arguments
    text = sys.argv[1]

    # Process any additional options
    invert = False
    width = 80

    for arg in sys.argv[2:]:
        if arg.startswith("-i") or arg == "--invert":
            invert = True
        elif arg.startswith("-w") or arg.startswith("--width="):
            try:
                width = int(arg.split("=")[1])
            except ValueError:
                print(f"Invalid width value: {arg}. Using default of 80.")
                width = 80

    # Generate ASCII art with the specified options
    ascii_art = generate_ascii_art(text, width)

    # Invert the string if requested
    if invert:
        inverted_text = invert_string(text)
        print(f"Inverted text: {inverted_text}")
    else:
        print(f"ASCII art generated from text: {text}")

    # Print the ASCII art
    print(ascii_art)

if __name__ == "__main__":
    main()
