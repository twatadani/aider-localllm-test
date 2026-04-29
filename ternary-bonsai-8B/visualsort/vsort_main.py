import sys
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 最大値を最後に移動
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # 最大値を最後に移動
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_random_numbers(count):
    # 20個のランダムな整数を生成
    return [random.randint(1, 100) for _ in range(count)]

def print_step(arr, step):
    # 現在のリストの状態を視覚的に表示
    print(f"ステップ {step}: {arr}")

def main():
    # コマンドラインオプションを処理
    if len(sys.argv) < 2:
        print("Usage: python vsort_main.py [-b] [-q] [-m]")
        return

    # コマンドラインオプションを解析
    options = {}
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            option = arg[1:]
            if option in ['b', 'q', 'm']:
                options[option] = True

    # ランダムな整数を生成
    numbers = generate_random_numbers(20)
    print(f"初期のリスト: {numbers}")

    # コマンドラインオプションに基づいてソートアルゴリズムを選択
    if options.get('-b', False):
        sorted_numbers = bubble_sort(numbers)
        print("バブルソートでソートしました")
    elif options.get('-q', False):
        sorted_numbers = quick_sort(numbers)
        print("クイックソートでソートしました")
    elif options.get('-m', False):
        sorted_numbers = merge_sort(numbers)
        print("マージソートでソートしました")
    else:
        sorted_numbers = numbers
        print("デフォルトのソートアルゴリズムを使用しました")

    # ソートの1ステップごとに状態を表示
    for step in range(1, 21):
        print_step(sorted_numbers, step)

if __name__ == '__main__':
    main()
