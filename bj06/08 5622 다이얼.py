'''
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
![img](https://upload.acmicpc.net/9c88dd24-3a4c-4a09-bc50-e6496958214d/-/preview/)

전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

예제 입력 1 
WA
예제 출력 1 
13
예제 입력 2 
UNUCIC
예제 출력 2 
36
'''

# 입력함수
words = input()

# 풀이1. 인덱스 활용 - 메모리 33548 KB, 시간 128 ms
def solution1(words):
    answer = 0 
    # 알파벳 다이얼 리스트 생성
    dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    # 입력 문자열에 대한 최소 시간 구하기
    for word in words: # 입력 문자열의 한 글자마다 돌면서
        for dial in dials: # 다이얼 리스트의 각 요소에
            if word in dial: # 해당 값이 있는지 확인
                answer += dials.index(dial) + 3 # 있다면, 다이얼 리스트의 인덱스에 + 3 을 더하기
    return answer

print(solution1(words))

# 참고: https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-5622%EB%B2%88-%EB%8B%A4%EC%9D%B4%EC%96%BC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython


# 풀이2. 문자형을 숫자형으로 변환 - 메모리 30840 KB, 시간 72 ms
def solution2(words):
    # 알파벳 다이얼 딕셔너리 생성 { '알파벳' : '번호' }
    dial = {'A': '2','B': '2','C' : '2', 'D' :'3','E' :'3','F' : '3', 'G':'4','H':'4','I' : '4', 'J': '5','K': '5','L': '5', 'M': '6','N': '6','O' : '6', 'P' : '7','Q' : '7','R' : '7','S' : '7','T': '8','U': '8','V' : '8', 'W' : '9','X' : '9','Y' : '9','Z' : '9'}
    
   # 입력 문자열을 딕셔너리의 숫자 문자로 변경
    num = str()
    for word in words:
        num += dial[word]

    # 숫자 문자열로 바뀐 데이터로 최소 시간 구하기
    answer = 0
    for i in num:           # 숫자 문자열의 각 글자마다
        answer += int(i)    # 정수형으로 바꿔 모두 더하기
    answer += len(num)      # 글자 개수마다 +1씩 더해 필요 시간 더하기
    return answer

print(solution2(words))


# 참고 : https://god-gil.tistory.com/30

