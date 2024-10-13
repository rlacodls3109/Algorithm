import sys

N = int(input())

card = list(map(int,sys.stdin.readline().split()))

M = int(input())

find = list(map(int,sys.stdin.readline().split()))

# 속도를 빠르게 개선하려면 딕셔너리가 효율적이다
check_dict = {}
for i in range(N):
    check_dict[card[i]] = 1

for j in range(M):
    if find[j] in check_dict:
        print(1, end= " ")
    else:
        print(0, end= " ")
