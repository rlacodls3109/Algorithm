a_1, a_0 = tuple(map(int,input().split()))
c = int(input())
n_0 = int(input())

def F1(n):
    return a_1*n + a_0

def G1(n):
    return n

result = 0

if F1(n_0) <= c*G1(n_0) and a_1 <= c:
    print(1)
else :
    print(0)