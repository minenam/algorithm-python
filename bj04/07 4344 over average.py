'''
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

예제 입력 1 
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

예제 출력 1 
40.000%
57.143%
33.333%
66.667%
55.556%
'''

import sys

C = int(input())

# 입력을 위한 함수
def inputs(C):
    inputs = []
    for i in range(C):
        inputs.append(list(map(int,sys.stdin.readline().rstrip().split())))
    return inputs

# 문제 출력 함수
def overAverage(cases):
    averageList = [] # 전체 평균 이상 비율 리스트
    for i in range(len(cases)):
        overScoreCount = 0 # 평균 이상 학생 수
        averageScore = sum(cases[i][1:]) / cases[i][0] # 케이스별 평균 점수
        for case in cases[i][1:]:
            if case > averageScore: # 평균보다 높은 경우, 학생 수 +1
                overScoreCount += 1
        averageRatio = round(overScoreCount / cases[i][0] * 100, 3) # 각 케이스별 평균 이상 학생 비율 (백분율, 반올림 소수점)
        averageList.append(f'{averageRatio:.3f}%') # 소수점 이하 세자리까지 출력
    return averageList

print('\n'.join(overAverage(inputs(C))))