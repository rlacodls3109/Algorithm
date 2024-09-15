n = int(input())

result = -1

# 1. 5로 나누어 떨어지는 경우
if n % 5 == 0 :
    result = n // 5


else : 
    count = 0
    while n > 0:
        # n이 0보다 클 동안 반복해서 3을 빼준다
        n -= 3
        count += 1

        # 2. 숫자가 3과 5를 조합해서 나올 수 있는 경우
        if n % 5 == 0:
            count += n // 5
            result = count
            break

        # 3. 3으로 나누어 떨어지는 경우
        elif n == 0 :
            result = count
            break
        
print(result)