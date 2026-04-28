import sys
import time

def calculate_progress(n):
    """指定された秒数nを処理し、進行度%と予定残り秒数を計算します。

    Args:
        n (int): ターミナルから受け取った秒数。

    Returns:
        tuple: (進行度%, 予定残り秒数)
    """
    start_time = time.time()
    elapsed_time = 0
    remaining_seconds = n

    while elapsed_time < n:
        # 時間を更新
        elapsed_time = time.time() - start_time

        # 進行度と残り秒数を計算
        progress_percent = (elapsed_time / n) * 100
        remaining_seconds = n - elapsed_time

        # プログレスバーを出力
        print(f"{'=' * int(progress_percent / 2)}{'.' * (10 - int(progress_percent / 2))} {progress_percent:.1f}% | 残り: {remaining_seconds:.1f}s")

        # 1秒ごとに更新
        time.sleep(1)

    # 最終的な進捗を出力
    print(f"{'=' * int(100 / 2)}{'.' * (10 - int(100 / 2))} 100% | 残り: {remaining_seconds:.1f}s")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python progress_main.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Usage: python progress_main.py <n>")
        sys.exit(1)

    calculate_progress(n)
