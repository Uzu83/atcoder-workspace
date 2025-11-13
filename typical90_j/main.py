import sys

#1 高速入力の準備
input = sys.stdin.readline

#2 Nを受けとる
n = int(input().rstrip())

#3. 累積和リストの初期化(サイズは n+1)
# index 0 は 「０人目」 = 「合計0点」として使う(番兵)
sum_1 = [0] * (n + 1)
sum_2 = [0] * (n + 1)

#4. 入力を受け取りながら、同時に累積和を作る
#学籍番号に合わせて１からnまでループ
for i in range(1, n + 1):
    c, p = map(int,input().split())

    #ここがポイント！
    #まず、直前の人(i-1)までの合計を引き継ぐ
    sum_1[i] = sum_1[i - 1]
    sum_2[i] = sum_2[i - 1]

    #その上で、今回の生徒の点数を該当クラスに加算する
    if c == 1:
        sum_1[i] += p
    else:
        sum_2[i] += p

#5. Qを受け取る
q = int(input().rstrip())

#6. クエリ処理
for _ in range(q):
    l, r = map(int, input().split())

    #累積和の公式: Sum[R] - Sum[L-1]
    #サイズをn+1にしたおかげで、L=1の時もL-1=0となりエラーにならない！
    ans_1 = sum_1[r] - sum_1[l - 1]
    ans_2 = sum_2[r] - sum_2[l - 1]

    print(f"{ans_1} {ans_2}")