import argparse
from random import randint
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from visualize_sort import print_step

def generate_random_numbers(count):
    """ランダムな整数を生成する関数"""
    return [randint(1, 100) for _ in range(count)]

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='ソートアルゴリズムの視覚化')
    parser.add_argument('-b', '--bubble', action='store_true', help='バブルソートを実行')
    parser.add_argument('-q', '--quick', action='store_true', help='クイックソートを実行')
    parser.add_argument('-m', '--merge', action='store_true', help='マージソートを実行')
    args = parser.parse_args()

    numbers = generate_random_numbers(20)
    print("ソート前のリスト:")
    print_step(numbers, 0)

    if args.bubble:
        bubble_sort(numbers, print_step)
    elif args.quick:
        quick_sort(numbers, 0, len(numbers) - 1, print_step)
    elif args.merge:
        merge_sort(numbers, 0, len(numbers) - 1, print_step)
    else:
        print("ソートアルゴリズムを選択してください。")
        return

    print("ソート後のリスト:")
    print_step(numbers, "完了")

if __name__ == "__main__":
    main()
