import sys


def solve():
    input = sys.stdin.readline
    N, K, X = map(int, input().split())
    A_list = list(map(int, input().split()))

    # 大きい順にソート
    A_list.sort(reverse=True)

    # 水が入ってるカップの個数
    num_water = N - K

    # 確実に確保できる日本酒の数
    current_sake = 0

    # num_water 個までは水である可能性があるので、
    # 確実に日本酒が得られる可能性があるのは num_water 番目の要素(0-indexed) から
    # つまり、(num_water + 1) 個目のカップからカウント開始

    # num_water 個未満しか選ばない場合、全部水かもしれないので日本酒は0
    # そのため、ループは num_water からスタートする
    for i in range(num_water, N):
        current_sake += A_list[i]

        # 目標を超えたら、その時の個数 (インデックス + 1) を出力
        if current_sake >= X:
            print(i + 1)
            return

    # 最後まで見ても X に届かなかった場合
    print(-1)


if __name__ == "__main__":
    solve()
