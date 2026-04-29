"""
ファクタリアル計算プログラムのメイン実行ファイルです。

コマンドライン引数として与えられた整数 n の階乗を計算し、ターミナルに出力します。
"""

import sys
from factorial import calculate_factorial

def main():
    """
    コマンドライン引数から整数を取得し、その階乗を計算して出力します。
    """
    # コマンドライン引数が正しく渡されているか確認します。
    if len(sys.argv) != 2:
        print("使用法: python factorial_main.py <非負整数>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("エラー: コマンドライン引数は整数でなければなりません。")
        sys.exit(1)
    
    # 階乗を計算します。
    result = calculate_factorial(n)
    
    # 結果をターミナルに出力します。
    print(f"{n} の階乗は {result} です。")

if __name__ == '__main__':
    main()
