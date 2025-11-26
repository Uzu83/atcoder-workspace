import sys
from collections import deque

def long_base_9(n):
    """int型の10進数の数をint型の9進数にして返す"""
    if n == 0:
        return(0)
    
    num_str = deque()
    while n > 0:
        num_str.appendleft(str(n % 9))
        n //= 9
        
    
    return int("".join(num_str))

def solve():
    N_str, K = input().split()
    K = int(K)
    if N_str == "0":
        print(0)
        return
    
    for _ in range(K):
        N_10 = int(N_str, 8)
        
        N_base_9 = long_base_9(N_10)
        
        N_str = str(N_base_9).replace("8", "5")
    
    print(N_str)

if __name__ == "__main__":
    solve()