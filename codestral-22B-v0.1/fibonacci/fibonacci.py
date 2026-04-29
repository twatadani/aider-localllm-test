def calculate_fibonacci(n):
    """指定された位置のフィボナッチ数を計算します。

    Args:
        n (int): 計算するフィボナッチ数の位置。

    Returns:
        int: 指定された位置のフィボナッチ数。
    """
    if n <= 0:
        return "無効な入力です。正の整数を入力してください。"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
