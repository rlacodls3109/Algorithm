import sys

n, m = tuple(map(int,input().split()))

chess_give = [
    list(input())
    for _ in range (n) 
]

final_result = sys.maxsize

# 시작점 i,j
for i in range(n-7):
    for j in range(m-7):
        first_W_count = 0
        first_B_count = 0
        result = sys.maxsize
        for a in range(i,i+8):
            for b in range(j,j+8):
                
                if ((a-i)+(b-j)) % 2 == 0:
                    if chess_give[a][b] != 'W':
                        first_W_count += 1
                    elif chess_give[a][b] != 'B':
                        first_B_count += 1
                    
                else :
                    if chess_give[a][b] != 'B':
                        first_W_count += 1
                    elif chess_give[a][b] != 'W':
                        first_B_count += 1
        
        result = min(first_B_count,first_W_count)
        
        final_result = min(result,final_result)
                

print(final_result)