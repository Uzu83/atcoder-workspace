import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. 前処理: 桁数ごとに余りをカウントする
    # cnt[d][r] := 桁数が d で, M で割った余りが r である数の個数
    # A_i <= 10^9 なので、桁数は最大10桁
    # 便宜上、cnt[1]...cnt[10]を使う。
    # 辞書(dict)を使うと、余りが疎な場合(Mが大きい場合)にもメモリを食わない
    cnt = [{} for _ in range(11)]

    for x in A:
        d = len(str(x))
        rem = x % M

        if rem not in cnt[d]:
            cnt[d][rem] = 0
        cnt[d][rem] += 1

    ans = 0

    # 2. 全探索 (ただし内側は桁数の10回だけ)
    for x in A:
        # 相手(A_j)の桁数を k (1~10) と仮定して全探索
        for k in range(1, 11):
            if not cnt[k]:
                continue

            # 式: (x * 10^k + A_j) % M == 0
            # 変形: A_j % M == (M - (x * 10^k % M)) % M

            term1 = (x * pow(10, k, M)) % M
            target_rem = (M - term1) % M

            # その桁数(k) で、余りが target_rem になる相手は何人いるか?
            if target_rem in cnt[k]:
                ans += cnt[k][target_rem]

    print(ans)


if __name__ == "__main__":
    solve()
