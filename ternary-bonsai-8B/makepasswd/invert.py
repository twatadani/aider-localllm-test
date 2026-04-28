import sys

def invert_string(s):
    """
    パスワードを逆にします。
    
    Args:
        s (str): パスワード
    
    Returns:
        str: 逆のパスワード
    """
    return s[::-1]

def main():
    """
    メイン処理です。
    
    コマンドラインからパスワードを読み取り、逆にします。
    """
    if len(sys.argv) < 2:
        print("Usage: python invert_main.py <password>")
        return
    
    password = sys.argv[1]
    inverted_password = invert_string(password)
    
    print(f"逆パスワード: {inverted_password}")

if __name__ == '__main__':
    main()
