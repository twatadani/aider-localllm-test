import sys
from factorial import calculate_factorial

def main():
    """
    コマンドライン引数で受け取った整数の階乗を計算してターミナルに出力する。
    """
    if len(sys.argv) != 2:
        print("Usage: python factorial_main.py <n>")
        sys.exit(1)

    n = int(sys.argv[1])
    result = calculate_factorial(n)
    print(f"{n}の階乗は{result}です。")

if __name__ == "__main__":
    main()
