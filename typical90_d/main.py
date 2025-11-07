#最初にH,Wを受け取る
h,w = map(int,input().split())

#次に、マップを受け取る
num_map = [list(map(int,input().split())) for _ in range(h) ]

#dp[i][j] は上からi行目,もしくは左からj行目にあるマスの値の合計値を示す。

dp =[[0 for _ in range(w)] for _ in range(h)]

print(dp)