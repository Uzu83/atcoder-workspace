import sys


def solve():
    input = sys.stdin.readline
    L, R = map(int, input().split())
    MOD = 10**9 + 7

    ans = 0

    # 桁数 i を 1 から 19 (10^18 は 19桁) までループ
    for i in range(1, 20):
        # i桁の整数の範囲[lower, upper]
        # 例: 2桁なら10 ~ 99
        lower = 10 ** (i - 1)
        upper = 10**i - 1

        # 今回のクエリ範囲 [L, R] と、i桁の範囲 [lower, upper] の重なりを求める
        # 重なり部分の左端 vl と 右端 vr
        vl = max(L, lower)
        vr = min(R, upper)

        # 重なりが存在する場合のみ計算
        if vl <= vr:
            # 区間内の整数の個数
            count = vr - vl + 1

            # 区間内の整数の和 (等差数列の和の公式)
            # (初項 + 末項) * 個数 // 2
            sum_val = (vl + vr) * count // 2

            # 和をMODで割っておく
            sum_val %= MOD

            # (桁数) * (和) を答えに加算
            ans += i * sum_val
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    solve()
