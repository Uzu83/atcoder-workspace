import sys 

# 高速入力の準備
input = sys.stdin.readline

#A,B,Cをリストで受け取り
num_list = list(map(int,input().split()))

#大きい順に並び変え出力
num_list.sort(reverse=True)

print("".join(map(str,num_list)))