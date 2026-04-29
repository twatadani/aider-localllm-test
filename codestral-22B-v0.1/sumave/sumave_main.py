import sys

def calculate_sum_and_average(numbers):
    """
    与えられた数値のリストの合計と平均を計算します。
    """
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

if __name__ == '__main__':
    # コマンドライン引数から数値を取得
    numbers = [float(num) for num in sys.argv[1:]]

    # 合計と平均を計算
    total, average = calculate_sum_and_average(numbers)

    # 結果を出力
    print(f"合計: {total}")
    print(f"平均: {average}")
