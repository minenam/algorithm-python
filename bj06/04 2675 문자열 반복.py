'''
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.

예제 입력 1 
2
3 ABC
5 /HTP
예제 출력 1 
AAABBBCCC
/////HHHHHTTTTTPPPPP
'''

import sys

## 입력
T = int(input()) # 첫째 줄: 테스트 케이스 개수
answer = [] # 최종 결과 리스트

def solution():
    for t in range(T): # 테스트 케이스 수 만큼 반복
        repeat, strings = sys.stdin.readline().rstrip().split() # 반복 횟수, 문자열을 입력받음
        result = ''
        for string in strings: # 테스트 케이스의 문자열 각 숫자에
            result += string * int(repeat) # 입력받은 반복 횟수를 곱함
        answer.append(result) # 테스트 케이스별 결과를 결과 리스트에 담음
    return answer # 최종 반환
    
# print('\n'.join(map(str,solution()))) # join과 map을 활용하여 결과 출력



## 다른방법 - find() 함수 : 메모리나 시간 차이 없음

# 입력
T = int(input()) # 첫째 줄: 테스트 케이스 개수
for _ in range(T):
    c, str = input().split()
    for s in str:
        print(int(c)*s, end='')
    print()

