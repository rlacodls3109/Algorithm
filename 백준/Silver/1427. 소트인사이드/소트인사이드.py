import sys

num = input()

#각 자리 수를 셀 count_list
count_list = [0] * 10

# 내림차 순 정렬이므로 9부터 인덱스 0 을 가지도록 한다.
for i in range(len(num)):
    n = int(num[i])
    count_list[9-n] += 1

# count 된 수만큼 각 자릿수 출력
for k in range(len(count_list)):
    print(str(9-k)*count_list[k],end="")




