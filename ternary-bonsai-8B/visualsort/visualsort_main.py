# ここに主実行ファイルの処理を追加
# 例: バブルソートを視覚的に表示する関数を呼び出す
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
