import sys

def solve():
    input = sys.stdin.readline
    
    N, X, Y = map(int,input().split())
    
    A_list = list(map(int,input().rstrip().split()))
    
    
    diff = Y - X
    for i in range(N):
        base = A_list[0] * X
        if ((A_list[i] * X) - base) % diff != 0:
            print(-1)
            return
    
    
    max_weight = min(A_list) * Y
    min_weight = max(A_list) * X
    
    if max_weight < min_weight:
        print(-1)
        return
    
    
    best_weight = max_weight - (max_weight % diff - (base % diff)) % diff
    
    if best_weight < min_weight:
        print(-1)
        return
    
    
    count = 0
    for i in range(N):
        count += (best_weight - A_list[i] * X) // diff
    
    
    print(count)


if __name__ == "__main__":
    solve()