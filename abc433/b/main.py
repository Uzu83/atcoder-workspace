import sys
input = sys.stdin.readline

N = int(input().rstrip())
A_line = list(map(int,input().rstrip().split()))

for i in range(N):
    for j in reversed(range(i)):
        if A_line[j] > A_line[i]:
            print(j+1)
            break

    else:
        print(-1)