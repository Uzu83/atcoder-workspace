import sys

input = sys.stdin.readline

N = int(input().rstrip())
A_list = list(map(int,input().split()))


# Asum_list[i] は　A_list[0]からA_list[i]までの区間の和
Asum_list = [0] * N
for i in range(N):
    Asum_list[i] = sum(A_list[:i])

count = 0
for l in range(N):
    for r in range(l, N):
        A_sum = Asum_list[r] - Asum_list[l-1]
        for i in range(l, r+1):
            if A_sum % A_list[i] == 0:
                break
        else:
            count += 1

print(count)