import sys

input = sys.stdin.readline

N = int(input().rstrip())

ans = 0
for i in range(N+1):
    ans += i
    
print(ans)