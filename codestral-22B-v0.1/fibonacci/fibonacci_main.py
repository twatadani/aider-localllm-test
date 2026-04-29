import sys
from fibonacci import calculate_fibonacci

if __name__ == '__main__':
    n = int(sys.argv[1])
    result = calculate_fibonacci(n)
    print(f'The {n}th element of the Fibonacci sequence is: {result}')
