import sys

#高速入力の準備
input = sys.stdin.readline

#N,Kを受けとる
n,k = map(int,input().split())

#Aの数列,Bの数列を受けとる
a_list = list(map(int,input().rstrip().split()))
b_list = list(map(int,input().rstrip().split()))

# ★修正ポイント★
# 合計の差ではなく、「個々の差の合計」を計算する
diff = 0

for a,b in zip(a_list,b_list):
    diff += abs(a-b)

if (diff % 2) == (k % 2) and diff <= k:
    print("Yes")
else:
    print("No")