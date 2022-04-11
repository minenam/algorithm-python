'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제)
입력
5
1 1
2 3
3 4
9 8
5 2

출력
2
5
7
17
7
'''
import sys

T = int(input())

result = []
def plus(T):
    for t in range(T):
        a, b = map(int, sys.stdin.readline().split())
        result.append(a+b)

def getResult(result):
    for i in range(len(result)):
        print(result[i])

plus(T)
getResult(result)
