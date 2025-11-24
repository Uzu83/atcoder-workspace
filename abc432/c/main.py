def solve():
    import sys
    input = sys.stdin.readline

    N, X, Y = map(int,input().split())

    weight_counts = list(map(int,input().rstrip().split()))

    for i in range(N):
        base = weight_counts[0] * X
        if (weight_counts[i] * X - base) % (Y - X) != 0:
            print(-1)
            return()

    max_weight = min(weight_counts) * Y
    min_weight = max(weight_counts) * X

    if max_weight < min_weight:
        print(-1)
        return()
    
    best_weight = max_weight - ((max_weight % (Y - X)) - (base % (Y - X)))%(Y-X)

    if best_weight < min_weight:
        print(-1)
        return()
    
    counts = 0
    for i in range(N):
        count = (best_weight - weight_counts[i] * X) // (Y - X)
        counts += count

    print(counts)

if __name__ == "__main__":
    solve()