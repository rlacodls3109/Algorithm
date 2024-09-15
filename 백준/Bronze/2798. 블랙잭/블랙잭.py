import sys

n, m = tuple(map(int,input().split()))

card = list(map(int,input().split()))

gap = sys.maxsize

for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            sum_card3 = card[i]+card[j]+card[k]

            if sum_card3 <= m and abs(m-sum_card3) < gap:
                gap = m-sum_card3
                ans = sum_card3

print(ans)
