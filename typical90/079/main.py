import sys


def solve():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A_map = [list(map(int, input().split())) for _ in range(H)]
    A_total = sum(sum(row) for row in A_map)
    B_map = [list(map(int, input().split())) for _ in range(H)]
    B_total = sum(sum(row) for row in B_map)

    if (A_total - B_total) % 4 != 0:
        print("No")
        return

    count = 0
    for i in range(H - 1):
        for j in range(W - 1):
            diff = B_map[i][j] - A_map[i][j]
            if diff != 0:
                A_map[i][j] += diff
                A_map[i][j + 1] += diff
                A_map[i + 1][j] += diff
                A_map[i + 1][j + 1] += diff
                count += abs(diff)
        else:
            if A_map[i][W - 1] != B_map[i][W - 1]:
                print("No")
                return
    else:
        if A_map[-1] != B_map[-1]:
            print("No")
            return
        else:
            print("Yes")
            print(count)


if __name__ == "__main__":
    solve()
