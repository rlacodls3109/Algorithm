N = int(input())

ans = 0

# 생성자 number을 for문을 통해 찾기
for number in range(1000000):
    # number의 각 자리수 합을 찾기 위해 문자열로 변환
    number_string = str(number)

    # 각 자리수의 합 sum_each 구하기
    sum_each = 0
    for i in range(len(number_string)):
        sum_each += int(number_string[i])
    
    # 생성자와 생성자의 각 자리수의 합 = 분해합 sum_final을 구한다 
    sum_final = number + sum_each

    # 분해합이 N과 같은 순간 가장 작은 생성자가 된다.
    if N == sum_final :
        ans = number
        break

print(ans)