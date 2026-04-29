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

def visualize_bubble_sort(arr):
    # バブルソートを視覚的に表示する関数
    for i in range(len(arr)):
        # 最大値を最後に移動
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # 最大値を最後に移動
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        print(f"ステップ {i+1}: {arr}")

def visualize_quick_sort(arr):
    # クイックソートを視覚的に表示する関数
    def quick_sort_helper(arr, low, high):
        if low < high:
            # パイボットのインデックスを計算
            pivot_idx = partition(arr, low, high)
            # 左側と右側を再帰的にソート
            quick_sort_helper(arr, low, pivot_idx - 1)
            quick_sort_helper(arr, pivot_idx + 1, high)

    def partition(arr, low, high):
        # パイボットを選び、左右の要素を比較
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                # 左側と右側を交換
                arr[i], arr[j] = arr[j], arr[i]
        # パイボットを最後に移動
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    # クイックソートを視覚的に表示
    quick_sort_helper(arr, 0, len(arr)-1)
    print("クイックソートでソートしました")

def visualize_merge_sort(arr):
    # マージソートを視覚的に表示する関数
    def merge_sort_helper(arr, left, right):
        if left < right:
            # 中間点を計算
            mid = (left + right) // 2
            # 左側と右側を再帰的にソート
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid+1, right)
            # 左側と右側をマージ
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        # マージの結果を計算
        result = []
        i = j = 0
        while i < mid - left + 1 and j < right - mid:
            if arr[left + i] <= arr[mid + j]:
                result.append(arr[left + i])
                i += 1
            else:
                result.append(arr[mid + j])
                j += 1
        # 剩りの要素を追加
        while i < mid - left + 1:
            result.append(arr[left + i])
            i += 1
        while j < right - mid:
            result.append(arr[mid + j])
            j += 1
        # マージ結果を元の配列にコピー
        for k in range(len(result)):
            arr[left + k] = result[k]

    # マージソートを視覚的に表示
    merge_sort_helper(arr, 0, len(arr)-1)
    print("マージソートでソートしました")

def visualize_default_sort(arr):
    # デフォルトのソートアルゴリズムを視覚的に表示
    sorted_numbers = bubble_sort(arr)
    print("バブルソートでデフォルトのソートアルゴリズムを使用しました")

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
        visualize_bubble_sort(numbers)
        print("バブルソートでソートしました")
    elif options.get('-q', False):
        visualize_quick_sort(numbers)
        print("クイックソートでソートしました")
    elif options.get('-m', False):
        visualize_merge_sort(numbers)
        print("マージソートでソートしました")
    else:
        visualize_default_sort(numbers)
        print("デフォルトのソートアルゴリズムを使用しました")

if __name__ == '__main__':
    main()
