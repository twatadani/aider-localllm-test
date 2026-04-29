def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Invalid input, please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
