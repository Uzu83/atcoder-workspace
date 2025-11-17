import sys

N = int(input().rstrip())
usernames = set()

for i in range(N):
    name = input().rstrip()
    if name not in usernames:
        usernames.add(name)
        print(i + 1)
        