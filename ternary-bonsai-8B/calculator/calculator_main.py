# メイン実行ファイル
# 評価式を評価するためのスクリプトを実行します

import sys
from calculator import calculate

def main():
    """
    メイン実行処理
    
    コマンドラインから入力式を取得し、評価します。
    """
    if len(sys.argv) < 2:
        print("Usage: python calculator_main.py <expression>")
    else:
        expression = sys.argv[1]
        result = calculate(expression)
        print(f"結果: {result}")

if __name__ == "__main__":
    main()
