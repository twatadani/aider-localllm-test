# sumave_main.py
# このスクリプトは、コマンドラインから複数の数値を読み取り、それらの合計と平均値を出力します。

import sys
from sumave import calculate_sum_and_average, invert_string

def main():
    """
    メイン処理を実行します。

    コマンドラインから受け取った数値は、整数または浮動小数点数で、1個以上いくつでも含まれます。
    出力は、合計と平均値の両方をターミナルに表示します。
    """
    if len(sys.argv) < 2:
        print("Usage: python sumave_main.py [numbers]")
        print("例: python sumave_main.py 1 2 3")
        return

    try:
        numbers = list(map(float, sys.argv[1:]))
    except ValueError:
        print("エラー: 全てのコマンドライン引数は数字でなければならない")
        return

    total, average = calculate_sum_and_average(numbers)
    print(f"合計: {total}")
    print(f"平均値: {average}")

if __name__ == '__main__':
    main()
