import sys


def solve():
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # 階差配列 B を作る
    # B[i] = A[i+1] - A[i] (つまり i番目と i+1番目の標高差)
    # Bのサイズは N-1 個
    B = []
    for i in range(N - 1):
        B.append(A[i + 1] - A[i])

    # 現在の不便さの総和をあらかじめ計算しておく
    ans = 0
    for val in B:
        ans += abs(val)

    for _ in range(Q):
        L, R, V = map(int, input().split())

        # 配列のインデックスに合わせるため -1 するが、
        # 階差配列 B は「隙間」の配列なので少し注意が必要

        # 1. 左端の処理 (L=1のときは左隣がないので無視)
        # L番目とその左(L-1番目)との差が変わる
        # 階差配列でいうと B[L-2] が該当
        if L > 1:
            # 更新前の値を答えから引く
            ans -= abs(B[L - 2])
            # 差分を更新 (右側 A[L-1] が V 増える = 差が V 増える)
            B[L - 2] += V
            # 更新後の値を答えに足す
            ans += abs(B[L - 2])

        # 2. 右端の処理 (R=Nのときは右隣がないので無視)
        # R番目とその右(R+1番目)との差が変わる
        # 階差配列でいうと B[R-1] が該当
        if R < N:
            # 更新前の値を答えから引く
            ans -= abs(B[R - 1])
            # 差分を更新 (左側 A[R-1] が V 増える = 差が V 減る)
            B[R - 1] -= V
            # 更新後の値を答えに足す
            ans += abs(B[R - 1])

        print(ans)


if __name__ == "__main__":
    solve()
