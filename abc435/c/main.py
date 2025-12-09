import sys

def solve():
    input == sys.stdin.readline
    
    N = int(input().rstrip())
    height = list(map(int,input().split()))
    
    count = 0
    is_hitted = [False] * N
    is_hitted[0] = True
    for i in range(N):
        if is_hitted[i] :
            is_hitted[i:i+height[i]] = [True] * height[i]
            count += 1
    
    print(count)


if __name__ == "__main__":
    solve()