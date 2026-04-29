import sys
from invert import reverse_string

def main():
    """
    コマンドライン引数で受け取った文字列を逆順にターミナルに出力するメイン関数。
    """
    input_string = sys.argv[1]
    reversed_string = reverse_string(input_string)
    print("入力文字列を逆順にした結果: ", reversed_string)

if __name__ == "__main__":
    main()
