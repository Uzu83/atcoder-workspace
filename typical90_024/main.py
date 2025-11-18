import sys
input = sys.stdin.readline

# NとKを受けとる
N, K = map(int,input().split())

# A数列とB数列を受け取り、要素の差の大きさの和を求める
A_list = list(map(int,input().rstrip().split()))
B_list = list(map(int,input().rstrip().split()))

diff = sum(abs(a-b) for a,b in zip(A_list,B_list))

if K >= diff and (K - diff) % 2 == 0:
    print("Yes")
else:
    print("No")