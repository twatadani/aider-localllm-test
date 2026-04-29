import os
import sys

def count_file_stats(filepath):
    """
    指定されたファイルのサイズ、行数、単語数、文字数を計算します。
    """
    # ファイルのサイズを計算
    size = os.path.getsize(filepath)

    # ファイルを開き、行数、単語数、文字数を計算
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum([len(line.split()) for line in lines])
        char_count = sum([len(line) for line in lines])

    return size, line_count, word_count, char_count

def main():
    """
    メイン関数。コマンドライン引数で指定されたファイルの統計情報を出力します。
    """
    if len(sys.argv) != 2:
        print("使い方: python filecount_main.py <ファイルパス>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("指定されたファイルが存在しません。")
        sys.exit(1)

    size, line_count, word_count, char_count = count_file_stats(filepath)
    print(f"ファイルサイズ: {size} バイト")
    print(f"行数: {line_count}")
    print(f"単語数: {word_count}")
    print(f"文字数: {char_count}")

if __name__ == "__main__":
    main()
