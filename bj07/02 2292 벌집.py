'''
문제
[https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png](https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png)

위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

예제 입력 1 
13
예제 출력 1 
3
예제 입력 2
58
예제 출력 2 
5
'''
# 입력함수
N = int(input())

# 내 풀이 -> 풀이 2 방법 채택
def solution(N):
    last = (N-1) / 6 # 각 층의 마지막 숫자를 규칙에 맡게 변형
    # 0, 1, 3, 6,.. 의 수열 a_n 일반항 : n*(n+1) / 2

    answer = 0
    while answer * (answer+1) / 2 < last:
        answer += 1
    
    return answer + 1

print(solution(N))


# 풀이1 : https://intrepidgeeks.com/tutorial/baijun-2292-honeycomb-bronze-2-python
def solution1():
    n = int(input())

    nums, cnt = 1, 1
    while n > nums:
        nums += 6 * cnt
        cnt += 1

    print(cnt)

# 풀이2 : https://www.acmicpc.net/board/view/79753
def solution2():
    n = int(input())
    k = (n-1)/6

    i=0
    while i*(i+1)/2<k:
        i+=1

    print(i+1)