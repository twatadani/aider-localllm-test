def partition(arr, low, high, print_step):
    """クイックソートのパーティション関数"""
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print_step(arr, f"パーティション {low}-{high}")
    return (i+1)

def quick_sort(arr, low, high, print_step):
    """クイックソートを実行する関数"""
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high, print_step)
        quick_sort(arr, low, pi-1, print_step)
        quick_sort(arr, pi+1, high, print_step)
