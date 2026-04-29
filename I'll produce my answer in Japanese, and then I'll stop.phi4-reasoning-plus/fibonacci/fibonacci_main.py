#!/usr/bin/env python3
"""
フィボナッチ数列のn番目の要素を計算するプログラムです。
コマンドライン引数でnを受け取り、計算した結果を出力します。
"""

import sys

def fibonacci(n):
    """
    フィボナッチ数列のn番目の要素を計算します。
    nは非負整数である必要があります。n=0の場合は0を返します。
    """
    if n < 0:
        raise ValueError("nは非負整数でなければなりません。")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

def main():
    """
    コマンドライン引数からnを受け取り、フィボナッチ数列のn番目の要素を計算して出力します。
    """
    if len(sys.argv) != 2:
        print("使用法: python fibonacci_main.py <n>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("エラー: 引数は整数でなければなりません。")
        sys.exit(1)
    result = fibonacci(n)
    print(f"フィボナッチ数列の{n}番目の要素は {result} です。")

if __name__ == '__main__':
    main()
