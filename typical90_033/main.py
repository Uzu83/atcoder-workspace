import sys
input = sys.stdin.readline

H, W = map(int,input().split())
# コーナーケース・チェック
# H=1 or W = 1の時,2x2の領域が作れない

if H == 1 or W == 1:
    print(H * W)
    exit()

ans = ((H + 1) // 2) * ((W + 1) // 2)

print(ans)