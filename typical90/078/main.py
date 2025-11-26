import sys

def solve():
    input = sys.stdin.readline
    
    N, M = map(int,input().split())
    
    next_list = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        
        next_list[a].append(b)
        next_list[b].append(a)
    
    ans = 0
    for i in range(1, N+1):
        count = 0
        for j in range(len(next_list[i])):
            if i > next_list[i][j]:
                count += 1
        
        if count == 1:
            ans += 1
    
    
    print(ans)


if __name__ == "__main__":
    solve()