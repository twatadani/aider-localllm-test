import sys
from gcd import gcd

def main():
    # コマンドラインから2つの数を取得
    if len(sys.argv) < 3:
        print("Usage: python gcd_main.py <m> <n>")
        return

    m = int(sys.argv[1])
    n = int(sys.argv[2])

    # 最大公約数を計算
    result = gcd(m, n)

    # 結果をターミナルに表示
    print(f"最大公約数: {result}")

if __name__ == "__main__":
    main()
