import sys
input = sys.stdin.readline

H, W = map(int,input().split())

grid = [list(map(int,input().rstrip().split())) for _ in range(H)]

row_sums = list(map(sum,grid))
col_sums = list(map(sum,zip(*grid)))

for i in range(H):
    l = []
    for j in range(W):
        l.append(str(row_sums[i] + col_sums[j] - grid[i][j]))

    print(" ".join(l))