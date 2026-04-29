import sys

def calculate_gcd(m, n):
    """ユークリッド互除法を用いて最大公約数を計算する関数

    Args:
        m (int): 最大公約数を計算する整数1
        n (int): 最大公約数を計算する整数2

    Returns:
        int: mとnの最大公約数
    """
    while n != 0:
        print(f"{m} = {m // n} * {n} + {m % n}")
        m, n = n, m % n
    return m

if __name__ == '__main__':
    # コマンドライン引数から整数mとnを取得
    m = int(sys.argv[1])
    n = int(sys.argv[2])

    # 最大公約数を計算して出力
    print(f"{m}と{n}の最大公約数は{calculate_gcd(m, n)}です。")
