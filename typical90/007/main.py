import sys
import bisect


def solve():
    input = sys.stdin.readline
    N = int(input().rstrip())
    rate_list = list(map(int,input().rstrip().split()))
    
    rate_list_sorted = sorted(rate_list)
    
    Q = int(input().rstrip())
    
    for _ in range(Q):
        B = int(input().rstrip())
        
        
        # bisect_left: B を挿入するならどこ? (index) を返す
        # つまり, rate_list_sorted[idx] >= B となる最初の場所
        idx = bisect.bisect_left(rate_list_sorted, B)
        
        # 答えの候補は以下の２つ
        # 1. idx番目の要素 (B以上の最小値)
        # 2. idx-1番目の要素 (Bより小さい最大値)
        
        diff1 = float('inf')
        diff2 = float('inf')
        
        if idx < N:
            diff1 = abs(B - rate_list_sorted[idx])
        
        if idx > 0:
            diff2 = abs(B - rate_list_sorted[idx - 1])
        
        print(min(diff1, diff2))

if __name__ == "__main__":
    solve()