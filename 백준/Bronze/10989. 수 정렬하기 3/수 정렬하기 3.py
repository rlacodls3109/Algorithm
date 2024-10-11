import sys

N = int(sys.stdin.readline())

'''
# 메모리 초과..
num_list = [
    int(sys.stdin.readline())
    for _ in range (N)
]
'''
'''
# 메모리 초과

count = [0] * (max(num_list)+1)

# 각 숫자 count 해서 배열에 담기
for num in num_list:
    count[num] += 1

# 누적 count를 계산해 count 배열을 갱신한다. 
# 현재 값에 이전 합계 더하기
for i in range(1,len(count)):
    count[i] += count[i-1]

# 정렬 결과 배열은 입력값의 개수만큼의 길이를 가져야 한다
result = [0] * N


for num in num_list:
    # 누적 count 배열의 값 = 결과 배열의 인덱스값
    # 0번째부터 정렬하므로 index - 1 해야 한다
    index = count[num]
    result[index-1] = num
    # 중복으로 나온 숫자의 정렬을 위해 -1 해준다.
    count[num] -= 1

#결과 출력
for j in range(N):
    print(result[j])

'''

count = [0] * 10001


# 각 숫자의 갯수 count
# num_list 만들 필요 없이 숫자 바로 입력받고 인덱스로 활용
for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

# 0~10000 까지 count 가 되지 않은 수 제외하고 count 된 만큼 출력한다.
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)

