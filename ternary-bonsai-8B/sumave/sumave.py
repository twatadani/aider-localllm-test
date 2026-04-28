# sumave.py
# このモジュールは、コマンドラインから複数の数値を読み取り、それらの合計と平均値を計算します。

def calculate_sum_and_average(numbers):
    """
    コマンドラインから受け取った数値を合計と平均値を計算します。

    Args:
        numbers (list): コマンドラインから受け取った数値のリスト

    Returns:
        tuple: (合計, 平均値)
    """
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

def invert_string(s):
    """
    テーミナルから受け取った文字列を逆にします。

    Args:
        s (str): テーミナルから受け取った文字列

    Returns:
        str: 反転後の文字列
    """
    return s[::-1]
