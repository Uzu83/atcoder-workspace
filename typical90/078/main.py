import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0
    for i in range(1, N + 1):
        count = 0
        for j in range(len(graph[i])):
            if graph[i][j] < i:
                count += 1

        if count == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
