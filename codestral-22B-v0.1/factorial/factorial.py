def calculate_factorial(n):
    """
    与えられた整数の階乗を計算する。
    """
    if n < 0:
        raise ValueError("階乗は負の数に対して定義されていません。")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
