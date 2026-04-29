import sys
from shutil import get_terminal_size

def convert_to_ascii(text):
    """入力テキストをASCIIアートに変換します。

    Args:
        text (str): 変換するテキスト。

    Returns:
        str: テキストのASCIIアート表現。
    """
    # ASCIIアートを中央に配置するためのターミナル幅を取得します。
    terminal_width = get_terminal_size().columns

    # アートに使用するASCII文字のリストを作成します。
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    # 入力テキストをASCIIアートに変換します。
    ascii_art = ''
    for char in text:
        # 各文字をASCIIアート表現にマッピングします。
        ascii_char = ascii_chars[ord(char) % len(ascii_chars)]
        # ASCIIアートを中央に配置するためにパディングを追加します。
        padding = ' ' * ((terminal_width - len(text)) // 2)
        ascii_art += padding + ascii_char * len(text) + '\n'
    return ascii_art

if __name__ == '__main__':
    # コマンドライン引数から入力テキストを取得します。
    input_text = ' '.join(sys.argv[1:])

    # 入力テキストをASCIIアートに変換し、出力します。
    ascii_art = convert_to_ascii(input_text)
    print(ascii_art)
