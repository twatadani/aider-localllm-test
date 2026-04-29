import sys

def evaluate_expression(expression):
    """
    この関数は、与えられた文字列を数式として評価し、結果を返します。
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print("式の評価中にエラーが発生しました:", str(e))
        return None

if __name__ == "__main__":
    # コマンドライン引数から式を取得
    expression = ' '.join(sys.argv[1:])

    # 式を評価して結果を取得
    result = evaluate_expression(expression)

    # 結果を出力
    if result is not None:
        print("結果:", result)
