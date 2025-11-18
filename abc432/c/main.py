import sys
input = sys.stdin.readline

# N, X, Yを受けとる
N, X, Y = map(int,input().split())

# A数列を受けとる
A_list = list(map(int,input().rstrip().split()))

# 数式 総重量をW,Xを配る数をx_numとする W = (A_list[i] - x_num) * Y + x_num * X

# 余りを確認(Y-Xごとの目盛りで,それにない重量は作れない)
diff = Y - X
remainder = (A_list[0] * X) % diff

for a in A_list[1:]:
    if (a * X) % diff != remainder:
        print(-1)
        exit()


# 最小の重量と最大の重量をチェック
min_weight = max(A_list) * X
max_weight = min(A_list) * Y

if min_weight >= max_weight:
    print(-1)
    exit()


# max_weight から「ズレ」を引く
best_weight = max_weight - (max_weight - remainder) % diff

if best_weight < min_weight:
    print(-1)
    exit()

# 答えの計算
total_large_candies = 0

for a in A_list:
    # (目標の重さ - 全部小さい時の重さ) ÷ (1個交換で増える重さ)
    # = その子が持つべき「大きな飴」の数
    count = (best_weight - a * X) // diff
    total_large_candies += count

print(total_large_candies)