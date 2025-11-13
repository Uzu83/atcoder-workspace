import sys
import math #Pythonの数学ライブラリ(最大公約数gcdを使うため)

#高速入力の準備
input = sys.stdin.readline

#1. A,B,Cを受けとる
a,b,c = map(int, input().split())

#2. 3つの数の最大公約数(GCD)を求める
#math.gcd(a,b)で２つのGCDが出せるので、入れ子にします
#rは、作れる立方体の「一辺の長さ」になります
r = math.gcd(a, math.gcd(b,c))

#3. カット回数を計算する
#(全体の長さ // 一辺の長さ) で「ピースの数」が出る。
#「カット回数」は「ピースの数 - 1」回。
#これをA,B,Cそれぞれについて計算して足す。

#計算式: (a//r - 1) + (b//r - 1) + (c//r - 1)
ans = (a//r - 1) + (b//r - 1) + (c//r - 1)

print(ans)
