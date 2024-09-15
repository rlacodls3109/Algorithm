n = int(input())

cnt = 0
number = 666 # 첫번째 영화의 이름은 무조건 666

while(1):
    # number을 string으로 변환했을 때, 666이라는 문자열이 있으면 count
    if '666' in str(number):
        cnt += 1
    
    # count 횟수가 n과 같아지면 종료한다.
    if cnt == n:
        break
    
    number += 1

print(number)