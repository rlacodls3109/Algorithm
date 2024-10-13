import copy
import sys

N = int(input())

# 좌표를 입력받는다
coord = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(N)
]

'''
# 시간 초과
for i in range(N):
    for j in range(i,N):
        # x좌표 비교, 리스트는 mutable한 자료구조이기 때문에, deepcopy로 값을 복사해주어야 한다.
        if coord[i][0] > coord[j][0]:
            temp = copy.deepcopy(coord[i])
            coord[i] = copy.deepcopy(coord[j])
            coord[j] = temp
        # x좌표가 같다면 y좌표 비교
        elif coord[i][0] == coord[j][0]:
            if coord[i][1] > coord[j][1]:
                temp = copy.deepcopy(coord[i])
                coord[i] = copy.deepcopy(coord[j])
                coord[j] = temp
'''

coord.sort()

# 결과 출력
for i in range(len(coord)):
    print(coord[i][0], coord[i][1])
