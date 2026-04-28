import sys
from factorial import calculate_factorial

def main():
    # コマンドラインからnを取得
    if len(sys.argv) < 2:
        print("Usage: python factorial_main.py <n>")
        return

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for n.")
        return

    # nの階乗を計算
    result = calculate_factorial(n)

    # 結果をターミナルに出力
    print(f"{n}の階乗は {result} です。")

if __name__ == "__main__":
    main()
