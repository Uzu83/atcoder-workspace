import sys
input = sys.stdin.readline

N, X, Y = map(int,input().split())
A_list = list(map(int,input().rstrip().split()))

diff = Y - X
for a in A_list:
    if ((A_list[0] * X) % diff) - ((a * X) % diff) != 0:
        print(-1)
        exit()

min_weights = max(A_list) * X
max_weights = min(A_list) * Y

if min_weights > max_weights:
    print(-1)
    exit()

best_weights = max_weights // diff * diff + ((A_list[0] * X) % diff)

if best_weights < min_weights:
    print(-1)
    exit()

ans = 0

for a in A_list:
    ans += (best_weights - a * X) // diff

print(ans)