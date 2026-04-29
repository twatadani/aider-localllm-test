import sys

def calculate_factorial(n):
    """
    指定された数字 n の階乗を計算する。

    Args:
        n (int): 計算対象の数字

    Returns:
        int: n の階乗
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(f"The factorial of {n} is: {calculate_factorial(n)}")
    except ValueError:
        print("Please provide a valid integer as command line argument.")
