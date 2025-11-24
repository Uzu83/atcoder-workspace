import sys
def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())


    # 1. グラフ (友達リスト) の箱を作る
    # graph[i] は 頂点 i に隣接する頂点のリスト
    graph = [[] for _ in range(N + 1)]


    # 2. 辺を受け取ってグラフを作る
    for _ in range(M):
        a, b = map(int, input().split())
        # a の友達に b を追加
        graph[a].append(b)
        # b の友達に a を追加 (双方向!)
        graph[b].append(a)


    # 3. 条件を満たす頂点を数える
    ans = 0
    for i in range(1, N + 1):
        # iばんめの頂点についてチェック
        # graph[i] の中にある「自分(i)より小さい数」を数える
        count_smaller = 0
        for neighbor in graph[i]:
            if neighbor < i:
                count_smaller += 1

        if count_smaller == 1:
            ans += 1
    

    print(ans)


if __name__ == "__main__":
    solve()