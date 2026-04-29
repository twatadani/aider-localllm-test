# 五目並べゲームの主実行ファイル
# プログラムは、ユーザーと対話的にゲームをプレイできるように設計されています

import gomoku

def main():
    """主実行関数。"""
    print("五目並べゲーム開始！")
    gomoku.play_game()

if __name__ == "__main__":
    main()
