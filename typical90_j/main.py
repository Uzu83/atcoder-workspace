import sys

#高速入力の準備
input = sys.stdin.readline

#1. Nを受けとる
n = int(input().rstrip())

#2. 累積割ストの初期化(サイズはn+1)
#sum_1[i] : 学籍番号i番までの 1組の合計点
sum_1 = [0] * (n + 1)
sum_2 = [0] * (n + 1)

#3. 入力を受け取りながら累積和を作る(ループを1つに統合!)
for i in range(1, n+1):
    c, p = map(int, input().split())

    #POINT: まず「前の人までの合計」をコピーして引き継ぐ
    sum_1[i] = sum_1[i-1]
    sum_2[i] = sum_2[i-1]

    #POINT: 今回の人の点数を該当するクラスの方だけに足す
    if c == 1:
        sum_1[i] += p
    else:
        sum_2[i] += p

#4. クエリ処理
q = int(input().rstrip())

for _ in range(q):
    l,r = map(int,input().split())
    #S[R] - S[L-1] で区間和を一発計算
    ans_1 = sum_1[r] - sum_1[l-1]
    ans_2 = sum_2[r] - sum_2[l-1]

    print(ans_1,ans_2)