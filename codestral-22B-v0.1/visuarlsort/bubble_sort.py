def bubble_sort(arr, print_step):
    """バブルソートを実行する関数"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print_step(arr, f"ステップ {i+1}")
