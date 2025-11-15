import sys
import math

#高速入力の準備
input = sys.stdin.readline

#A,B,Cの受け取り
a,b,c = map(int,input().split())

#最大公約数を求める
d = math.gcd(a,math.gcd(b,c))

#切る回数を計算
count_cut = (a // d - 1) + (b // d - 1) + (c // d - 1)

#出力
print(count_cut)