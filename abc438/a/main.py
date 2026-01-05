d, f = map(int, input().split())
ans = (7 - (d % 7) + f) % 7
if ans == 0:
    ans = 7
print(ans)
