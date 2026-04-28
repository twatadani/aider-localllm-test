# フィボナッチ数列を計算する主スクリプト

import sys
from fibonacci import fibonacci

def main():
    """
    コマンドラインからnを読み取り、フィボナッチ数列のn番目の要素を計算します。
    """
    if len(sys.argv) != 2:
        print("Usage: python fibonacci_main.py <n>")
        print("例: python fibonacci_main.py 7")
        return

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("エラー: <n>は整数でなければなりません。")
        return

    if n < 0:
        print("エラー: <n>は非負数でなければなりません。")
        return

    result = fibonacci(n)
    print(f"n={n}のフィボナッチ数: {result}")

if __name__ == "__main__":
    main()
