import sys

#H,Wを受け取る
h,w = map(int,sys.stdin.readline().split())

#マス目の整数を受け取る
num_map = []

for i in range(h):
    s = list(map(int,input().split())) #sys.stdin.readline()使いたかった；；
    num_map.append(s)

#各行の和、各列の和を計算する
w_sum = [0] * h
h_sum = [0] * w

for i in range(h):
    for j in range(w):
        w_sum[i] += num_map[i][j]
        h_sum[j] += num_map[i][j]

#結果を計算して１行ごとに出力する

for i in range(h):
    s = []
    for j in range(w):
        a = w_sum[i] + h_sum[j] - num_map[i][j]
        s.append(str(a))

    print(" ".join(s))