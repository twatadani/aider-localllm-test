import sys
from invert import invert_string

def main():
    # コマンドラインから文字列を取得
    if len(sys.argv) < 2:
        print("Usage: python invert_main.py <string>")
        return

    input_string = sys.argv[1]

    # 文字列を逆順に処理
    reversed_string = invert_string(input_string)

    # 逆順文字列をターミナルに出力
    print(reversed_string)

if __name__ == "__main__":
    main()
