import sys
import random
import string

def generate_password(length):
    """
    セキュアなパスワードを生成します。
    
    パスワードは小文字、大文字、記号、数字を含みます。
    パスワードの長さは指定された値に一致します。
    
    Args:
        length (int): パスワードの長さ
    
    Returns:
        str: 生成されたパスワード
    """
    # 小文字、大文字、記号、数字を含むすべての可能なキャラクター
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # 指定された長さのパスワードを生成
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    """
    メイン処理です。
    
    コマンドラインから文字数nを読み取り、その長さぴったりのパスワードを生成して出力します。
    """
    if len(sys.argv) < 2:
        print("Usage: python makepasswd_main.py <length>")
        return
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Usage: python makepasswd_main.py <length>")
        return
    
    if n <= 0:
        print("Usage: python makepasswd_main.py <length>")
        return
    
    password = generate_password(n)
    print(f"生成されたパスワード: {password}")

if __name__ == '__main__':
    main()
