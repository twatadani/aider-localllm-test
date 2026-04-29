import sys
from directory_traversal import get_size, print_directory_structure

def main():
    """
    このスクリプトは、指定されたディレクトリの構造とサイズを表示します。
    コマンドライン引数としてディレクトリのパスを受け取ります。
    """
    if len(sys.argv) != 2:
        print("使用法: python dtree_main.py <ディレクトリのパス>")
        sys.exit(1)

    directory_path = sys.argv[1]
    print("ディレクトリ構造:")
    print_directory_structure(directory_path)
    print("\nディレクトリサイズ:")
    print(f"{get_size(directory_path)} バイト")

if __name__ == "__main__":
    main()
