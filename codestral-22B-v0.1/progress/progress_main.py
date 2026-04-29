import sys
import time

def progress(seconds):
    """ターミナルに進行度バーを表示します。

    Args:
        seconds (int): 進行度バーを実行する秒数。
    """
    for i in range(seconds):
        # 完了した割合を計算します。
        percent = (i / seconds) * 100
        # 進行度バーに表示する '#' 文字の数を計算します。
        hashes = '#' * int(percent / 10)
        # 進行度バーに表示する '.' 文字の数を計算します。
        dots = '.' * (10 - len(hashes))
        # 残りの秒数を計算します。
        remaining = seconds - i - 1
        # 進行度バーと残りの秒数を表示します。
        print(f'\r[{hashes}{dots}] {percent:.0f}% ({remaining} 秒残り)', end='')
        # 1秒待機します。
        time.sleep(1)
    print()

if __name__ == '__main__':
    # コマンドライン引数から秒数を取得します。
    seconds = int(sys.argv[1])
    progress(seconds)
