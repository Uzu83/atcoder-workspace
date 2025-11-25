import sys
input = sys.stdin.readline

N, M = map(int,input().split())

num_l = [int(x) for x in input().rstrip().split()]

count = 0

ans_map = [[False] * (N * 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        num = int(str(num_l[i]) + str(num_l[j]))
        if num % M == 0:
            count += 1

print(count)
