import sys

N = int(input())

# 회원정보를 입력받는다

customer = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    a = int(a)
    customer.append((a,b))


customer.sort(key = lambda x: x[0])

# 결과 출력
for i in range(len(customer)):
    print(customer[i][0], customer[i][1])
