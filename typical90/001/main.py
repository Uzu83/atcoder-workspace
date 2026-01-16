import sys


def solve():
    input = sys.stdin.readline

    # N: 切れ目の数, L: ようかんの長さ
    # K: 選ぶ切れ目の数
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    # 判定関数: すべてのピースを x cm以上にして、K回以上切れるか？
    # True なら達成可能、False なら不可能
    def check(x):
        count = 0  # 切った回数（できたピースの数 - 1）
        pre = 0  # 前回の切れ目の位置（最初は0）

        for a in A:
            # 前回の切れ目からの長さが x 以上なら切る
            if a - pre >= x:
                count += 1
                pre = a  # 切れ目位置を更新

        # 最後のピース（最後の切れ目から L まで）の長さチェック
        if L - pre >= x:
            # 最後のピースも条件を満たすなら、有効なピースとしてカウントできる
            # つまり、ここまでで count 個の切れ目を入れられたということは
            # count + 1 個のピースができている
            pass
        else:
            # 最後のピースが短すぎる場合、その前の切れ目は無効にせざるを得ない
            # （実際には単に個数が足りない判定になればよい）
            pass

        # 実際に作れた「長さx以上のピースの数」を数える
        # 上記ループだと「切った回数」を数えている。
        # 正確には「x以上の区間がいくつ取れるか」を貪欲に数える。

        num_pieces = 0
        pre = 0
        for a in A:
            if a - pre >= x:
                num_pieces += 1
                pre = a

        # 最後の区間チェック
        if L - pre >= x:
            num_pieces += 1

        # K+1個以上のピースが作れるならOK
        return num_pieces >= K + 1

    # 二分探索
    # 答えの範囲は 1 〜 L
    left = 1
    right = L
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            # mid の長さで切れるなら、もっと長くできるか試す
            ans = mid
            left = mid + 1
        else:
            # 無理なら、長さを短くする
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    solve()
