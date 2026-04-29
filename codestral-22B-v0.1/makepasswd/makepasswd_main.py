import sys
import random
import string

def generate_password(length):
    """
    指定された長さのセキュアなパスワードを生成します。
    パスワードは小文字、大文字、数字、記号を含みます。
    """
    # パスワードに使用する文字セットを定義
    characters = string.ascii_letters + string.digits + string.punctuation
    # 指定された長さのパスワードを生成
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    # コマンドライン引数からパスワードの長さを取得
    length = int(sys.argv[1])
    # パスワードを生成して出力
    password = generate_password(length)
    print("Generated password:", password)
