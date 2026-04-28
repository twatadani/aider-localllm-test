import sys

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python factorial_main.py <n>")
    else:
        try:
            n = int(sys.argv[1])
            if n < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(factorial(n))
        except ValueError:
            print("Please provide a valid integer as the argument.")
