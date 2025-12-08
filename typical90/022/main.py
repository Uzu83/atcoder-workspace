import sys
import math
input = sys.stdin.readline

A, B, C = map(int,input().split())

d = math.gcd(A, B, C)

print((A // d - 1) + (B // d - 1) + (C // d - 1))