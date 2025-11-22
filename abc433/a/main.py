import sys
input = sys.stdin.readline

X, Y, Z = map(int,input().split())

if X < Y * Z:
    print("No")
elif (X - Z * Y) % (Z - 1) == 0:
    print("Yes")
else:
    print("No")