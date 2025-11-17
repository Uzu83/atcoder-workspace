import sys

#高速入力の準備
input = sys.stdin.readline

#数字を受け取り、リストにする
num_str_list = list(input().rstrip())
num_set = set(num_str_list)
if "0" in num_set:
    firstnum = sorted(num_set)[1]
    num_str_list.remove(firstnum)
    num_str_list.sort()
    num_str_list.insert(0,firstnum)
    print("".join(num_str_list))
else:
    num_str_list.sort()
    print("".join(num_str_list))
