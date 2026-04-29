# ここに視覚的なソートアルゴリズムの実装を追加
# 例: バブルソートの視覚的表示
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

# 他のソートアルゴリズムの視覚的表示関数を追加
