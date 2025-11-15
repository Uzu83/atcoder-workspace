import sys

#高速入力の準備
input = sys.stdin.readline

#1. H,Wを受け取る
h, w = map(int, input().split())

#2. マップを受け取る
num_map = [list(map(int, input().split())) for _ in range(h)]

#3. 前計算(ここがPythonicポイント!)
#行の和: 各行(row)に対して sum() を適用
w_sum = list(map(sum, num_map))

#列の和: zip(*num_map)で行列を「転置(縦横入れ替え)」してからsum() を適用
# *num_map でリストを展開し、zipで同じインデックスの要素をまとめる
h_sum = list(map(sum, zip(*num_map)))

#4. 答えを計算し出力する(ここは同じ)
for i in range(h):
    answer_line = []
    for j in range(w):
        #w_sum[i] + h_sum[j] - num_map[i][j]
        answer_line.append(str(w_sum[i] + h_sum[j] - num_map[i][j]))

    print(" ".join(answer_line))
    