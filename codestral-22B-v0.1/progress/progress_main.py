import sys
import time

def progress(seconds):
    """Display a progress bar in the terminal.

    Args:
        seconds (int): The number of seconds to run the progress bar.
    """
    for i in range(seconds):
        # Calculate the percentage completed.
        percent = (i / seconds) * 100
        # Calculate the number of '#' characters to display in the progress bar.
        hashes = '#' * int(percent / 10)
        # Calculate the number of '.' characters to display in the progress bar.
        dots = '.' * (10 - len(hashes))
        # Calculate the remaining seconds.
        remaining = seconds - i - 1
        # Print the progress bar and the remaining seconds.
        print(f'\r[{hashes}{dots}] {percent:.0f}% ({remaining} seconds remaining)', end='')
        # Wait for one second.
        time.sleep(1)
    print()

if __name__ == '__main__':
    # Get the number of seconds from the command line argument.
    seconds = int(sys.argv[1])
    progress(seconds)
