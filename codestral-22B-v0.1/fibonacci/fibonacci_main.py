import sys
from fibonacci import calculate_fibonacci

if __name__ == '__main__':
    n = int(sys.argv[1])
    result = calculate_fibonacci(n)
    print(f'フィボナッチ数列の{n}番目の要素は: {result}')
