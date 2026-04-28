import sys
from progress import calculate_progress

def main():
    """主実行関数。コマンドラインから秒数nを受け取り、進行度をターミナルで表示します。

    Args:
        n (int): ターミナルから受け取った秒数。
    """
    if len(sys.argv) < 2:
        print("Usage: python progress_main.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Usage: python progress_main.py <n>")
        sys.exit(1)

    calculate_progress(n)

if __name__ == '__main__':
    main()
