# フィボナッチ数列を計算するモジュール

def calculate_fibonacci(n):
    """
    フィボナッチ数列のn番目の要素を計算します。

    参数:
        n (int): フィボナッチ数列の位置（0から始まる）

    戻り値:
        int: n番目のフィボナッチ数
    """
    # フィボナッチ数列を計算するアルゴリズム
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# フィボナッチ数列を計算する関数
def fibonacci(n):
    """
    フィボナッチ数列のn番目の要素を計算します。

    参数:
        n (int): フィボナッチ数列の位置（0から始まる）

    戻り値:
        int: n番目のフィボナッチ数
    """
    return calculate_fibonacci(n)
