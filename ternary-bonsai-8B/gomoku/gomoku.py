# 五目並べゲームの主モジュール
# プログラムは、ユーザーと対話的にゲームをプレイできるように設計されています

def create_board(size=5):
    """5x5の五目並べゲーム盤を生成します。
    
    Args:
        size (int): ボードのサイズ（5x5をデフォルトとします）
    
    Returns:
        list: ボードの2D配列（0で空、1で黒、-1で白）"""
    return [[0 for _ in range(size)] for _ in range(size)]

def print_board(board):
    """ゲーム盤をターミナルで表示します。
    
    Args:
        board (list): ボードの2D配列"""
    for row in board:
        print(" ".join(str(cell) for cell in row))

def is_valid_move(board, row, col):
    """指定された位置が空であるか確認します。
    
    Args:
        board (list): ボードの2D配列
        row (int): 行番
        col (int): 列番
    
    Returns:
        bool: 空であるか"""
    return board[row][col] == 0

def make_move(board, row, col, player):
    """指定された位置にプレイヤーのマークを置きます。
    
    Args:
        board (list): ボードの2D配列
        row (int): 行番
        col (int): 列番
        player (str): プレイヤーのID（"X"や "O"）"""
    board[row][col] = player

def check_winner(board, player):
    """指定されたプレイヤーが勝ったか確認します。
    
    Args:
        board (list): ボードの2D配列
        player (str): 勝ちプレイヤーID（"X"または "O"）"""
    # 行
    for row in board:
        if all(cell == player for cell in row):
            return True
    # 列
    for col in range(len(board)):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    # 主対角線
    if all(board[i][i] == player for i in range(len(board))):
        return True
    # 反対の主対角線
    if all(board[i][len(board)-1-i] == player for i in range(len(board))):
        return True
    return False

def is_draw(board):
    """ゲームが引き分けになったか確認します。
    
    Args:
        board (list): ボードの2D配列"""
    return all(cell != 0 for row in board for cell in row)

def play_game():
    """主ゲームルーブを実行します。"""
    board = create_board()
    print("五目並べゲーム開始！")
    print_board(board)
    
    # プレイヤーの選択
    player = input("先手はX、後手はO。どちらが先手ですか？ (X/O) ").strip().upper()
    if player not in ("X", "O"):
        print("無効な選択です。XまたはOを入力してください。")
        return
    
    # プレイヤーのID
    current_player = player
    other_player = "O" if current_player == "X" else "X"
    
    # ゲームループ
    while True:
        print(f"\n{current_player}'s turn")
        try:
            row = int(input("行番（0-4）を入力してください: "))
            col = int(input("列番（0-4）を入力してください: "))
        except ValueError:
            print("無効な入力です。数字を入力してください。")
            continue
        
        if not is_valid_move(board, row, col):
            print("その位置は空ではありません。別の場所を選んでください。")
            continue
        
        make_move(board, row, col, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"{current_player}が勝ちました！")
            break
        elif is_draw(board):
            print("引き分けです。どちらが勝つかは分かりません。")
            break
        
        # プレイヤーを切り替える
        current_player, other_player = other_player, current_player

def main():
    """主実行関数。"""
    play_game()

if __name__ == "__main__":
    main()
