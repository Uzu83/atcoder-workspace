import sys

def solve():
    input = sys.stdin.readline
    
    N, X, Y = map(int,input().split())
    weight_list = list(map(int,input().rstrip().split()))
    
    
    # 余りチェック
    base = weight_list[0] * X
    diff = Y - X
    for i in range(1,N):
        if (weight_list[i] * X - base) % diff != 0:
            print(-1)
            return
    
    
    # 最大値・最小値チェック
    max_weights = min(weight_list) * Y
    min_weights = max(weight_list) * X
    
    if max_weights < min_weights:
        print(-1)
        return
    
    
    # 最適重量計算
    best_weights = max_weights - ((max_weights - base) % diff)
    
    
    # 範囲内かチェック
    if best_weights < min_weights:
        print(-1)
        return
    
    
    # 錘の個数計算
    Y_count = 0
    for i in range(N):
        Y_count += (best_weights - (weight_list[i] * X)) // diff
    
    print(Y_count)

if __name__ == "__main__":
    solve()