import sys
import itertools


def solve():
    """
    方針:
    N <= 10 なので、選手の並び順(順列)を全探索する
    計算量は O(N! * N)。 10! ≒ 3.6 * 10^6 なのでPythonでも5秒あれば余裕。
    """
    input = sys.stdin.readline
    n = int(input())
    run_times = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())

    # 2. 仲が悪いペアの管理 (隣接行列)
    bad_relation = [[False] * n for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        bad_relation[x][y] = True
        bad_relation[y][x] = True

    # 最小タイムの初期値
    min_total_time = float("inf")

    # 3. 順列全探索
    # p は [0, 1, 2, ...]のような選手IDの並び
    for p in itertools.permutations(range(n)):
        current_time = 0
        is_possible = True

        # 第1区間
        current_time += run_times[p[0]][0]

        # 第2区間以降
        for j in range(1, n):
            prev_runner = p[j - 1]
            curr_runner = p[j]

            # 不仲チェック
            if bad_relation[prev_runner][curr_runner]:
                is_possible = False
                break

            # タイム加算 (選手 p[j] が 第 j 区間を走る)
            current_time += run_times[curr_runner][j]

            # 枝刈り
            if current_time >= min_total_time:
                is_possible = False
                break

        # 記録更新
        if is_possible:
            if current_time < min_total_time:
                min_total_time = current_time

    # 4. 結果出力
    if min_total_time == float("inf"):
        print(-1)
    else:
        print(min_total_time)


if __name__ == "__main__":
    solve()
