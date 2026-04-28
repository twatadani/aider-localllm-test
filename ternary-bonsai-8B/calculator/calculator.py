# 評価式を評価するPythonスクリプト
# コマンドライン引数で入力式を受け取り、結果を出力します

def calculate(expression):
    """
    評価式を計算し、結果を返します。
    
    Args:
        expression (str): 評価式（例: "2 + 3", "5 * 6", "10 ** 2"など）
        
    Returns:
        str: 評価結果の文字列
    """
    try:
        # 表記式を評価するための関数を使用
        result = eval(expression)
        return str(result)
    except Exception as e:
        # 評価式が正しくない場合、エラーを返します
        return f"エラー: {str(e)}"

if __name__ == "__main__":
    # コマンドラインから入力式を取得
    if len(sys.argv) < 2:
        print("Usage: python calculator.py <expression>")
    else:
        expression = sys.argv[1]
        result = calculate(expression)
        print(f"結果: {result}")
