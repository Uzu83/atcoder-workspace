import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
A = list(map(int,input().rstrip().split()))

diff_Y_X = Y - X

# ステップ２: 余りチェック
remainder = (A[0] * X) % diff_Y_X
for a in A:
    if (a * X) % diff_Y_X != remainder:
        print(-1)
        exit()

# ステップ３: 共通範囲を探す
min_weights = []
max_weights = []
for a in A:
    min_weights.append(a * X)
    max_weights.append(a * Y)

min_possible_weight = max(min_weights)
max_possible_weight = min(max_weights)

if min_possible_weight > max_possible_weight:
    print(-1)
    exit()

# ステップ4: 最大の共通重さを見つける
best_weight = max_possible_weight - (max_possible_weight - remainder) % diff_Y_X

# ステップ5: 最終チェック
if best_weight < min_possible_weight:
    print(-1)
    exit()

# 答えの計算
total_large_candies = 0
for a in A:
    total_large_candies += (best_weight - a * X) // diff_Y_X

print(total_large_candies)