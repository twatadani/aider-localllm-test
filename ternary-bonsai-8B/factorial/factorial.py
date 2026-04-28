def calculate_factorial(n):
    """
    nの階乗を計算する関数。

    参数:
        n (int): 階乗の数。n >= 0

    返回:
        int: nの階乗
    """
    # nが0の場合、1を返す（0! = 1）
    if n == 0:
        return 1

    # nが正数の場合、階乗を計算
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
