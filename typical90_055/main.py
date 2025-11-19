import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())
A = [int(x) % P for x in input().split()]

ans = 0

# 5重ループ
for i in range(N):
    m1 = A[i]

    for j in range(i+1, N):
        m2 = (m1 * A[j]) % P

        for k in range(j+1, N):
            m3 = (m2 * A[k]) % P

            for l in range(k+1, N):
                m4 = (m3 * A[l]) % P

                for m in range(l+1, N):
                    if (m4 * A[m]) % P == Q:
                        ans += 1

print(ans)