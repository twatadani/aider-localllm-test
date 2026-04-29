# phi4-reasoning-plus/factorial/factorial.py
"""
ファクタリアルを計算するモジュールです。

このモジュールは、与えられた整数 n の階乗を計算する関数 calculate_factorial を提供します。
"""

def calculate_factorial(n):
    """
    与えられた整数 n の階乗を計算します。

    引数:
        n (int): 計算する階乗の対象となる非負整数です。

    戻り値:
        int: n の階乗を表す整数です。

    注意:
        n が負の場合はエラーを発生させます。
    """
    if n < 0:
        raise ValueError("負の整数に対する階乗は定義されていません。")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# テスト用コード（コメントアウトしてください）
# if __name__ == '__main__':
#     print(calculate_factorial(5))
