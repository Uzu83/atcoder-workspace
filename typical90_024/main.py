import sys

# 高速入力
input = sys.stdin.readline

# N, Kの受け取り(カンマの後にスペース)
n, k = map(int,input().split())

# 数列 A, B の受け取り
A = list(map(int,input().rstrip().split()))
B = list(map(int,input().rstrip().split()))

# 各要素の差の大きさの和を求める(Pythonic way!)

diff_sum = sum(abs(a - b) for a, b in zip(A, B))

# 判定
# 1. diff_sum <= k : 最短手数で届くか?
# 2. (k - diff_sum) % 2 == 0 : 余った手数を「行って戻る」で消費できるか? (パリティチェック)
if diff_sum <= k and (k - diff_sum) % 2 == 0:
    print("Yes")
else:
    print("No")