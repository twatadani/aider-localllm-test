def gcd(a, b):
    """
    ユークリッド互除法を使用して最大公約数を計算します。

    Args:
        a (int): 第1の数
        b (int): 第2の数

    Returns:
        int: aとbの最大公約数
    """
    # ユークリッド互除法を実装
    # aとbの順序を調整して、常にa > bとなるようにします
    if a < b:
        a, b = b, a

    # ユークリッド互除法の計算プロセスを表示
    print(f"計算中: a={a}, b={b}")

    while b != 0:
        # aとbの順序を調整
        if a < b:
            a, b = b, a

        # 余分を計算
        remainder = a % b
        print(f"ステップ: a={a}, b={b} → 余数 {remainder}")

        # aとbを更新
        a, b = b, remainder

    # 最大公約数が計算結果
    print(f"最大公約数: {a}")
    return a
