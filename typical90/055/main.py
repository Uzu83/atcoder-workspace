def solve():
    import sys
    input = sys.stdin.readline

    N, P, Q = map(int,input().split())

    nums = [int(x) % P for x in input().rstrip().split()]

    counts = 0

    for i in range(N):
        a1 = nums[i]
        for j in range(i+1,N):
            a2 = a1 * nums[j] % P
            for k in range(j+1,N):
                a3 = a2 * nums[k] % P
                for l in range(k+1,N):
                    a4 = a3 * nums[l] % P
                    for m in range(l+1,N):
                        a5 = a4*nums[m] % P
                        if a5 == Q:
                            counts += 1

    print(counts)

if __name__ == "__main__":
    solve()