n = int(input())

result = -1

if n % 5 == 0 :
    result = n // 5

else : 
    count = 0
    while n > 0:
        n -= 3
        count += 1

        if n % 5 == 0:
            count += n // 5
            result = count
            break

        elif n == 0 :
            result = count
            break
        
print(result)