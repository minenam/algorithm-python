'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

예제)
입력
5
1 1
2 3
3 4
9 8
5 2

출력
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
'''

import sys

T = int(input())
result = []

def ABSum7(T):
    for t in range(T):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        result.append(A+B)
    for i in range(len(result)):
        print(f'Case #{i+1}: {result[i]}')
    
ABSum7(T)