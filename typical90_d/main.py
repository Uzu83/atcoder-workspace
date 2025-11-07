#最初にH,Wを受け取る
h,w = map(int,input().split())

#次に、マップを受け取る
num_map = [list(map(int,input().split())) for _ in range(h) ]

#ans[i][j] は上からi行目,もしくは左からj行目にあるマスの値の合計値を示す。
#(レビュー:この変数は推奨コードでは使わないのでコメントアウト)
ans_map =[[0 for _ in range(w)] for _ in range(h)]

#w_sum[i]は上からi行目のマスの値の合計値を示す。
w_sum = [0] * h

#h_sum[j]は左からj列目のマスの値の合計値を示す。
h_sum = [0] * w

#1回目のループ(前計算)
for i in range(h):
    for j in range(w):
        w_sum[i] += num_map[i][j]
        h_sum[j] += num_map[i][j]

#2回目のループ(計算と出力)
for i in range(h):
    #i行目の答えを格納する一時的なリスト
    ans_row = []
    for j in range(w):
        #ans_map[i][j] = w_sum[i] + h_sum[j] - num_map[i][j] #なんかわざわざこれする必要あるかな...?2重ループ２回回さなくてよくない?
        ans = w_sum[i] + h_sum[j] - num_map[i][j]
        ans_row.append(ans)
    
    # --- ここが出力のキモ！ ---
    # ans_row は [5, 5, 5] のような数値(int)のリスト
    # 1. map(str, ans_row) で、['5', '5', '5'] のように文字列(str)のリストに変換
    # 2. ' '.join(...) で、それらを ' ' (半角スペース) で連結して "5 5 5" という文字列にする
    print(' '.join(map(str,ans_row)))

#print(ans_map) #どうやって出力形式を半角スペース区切りにするんだ...?

