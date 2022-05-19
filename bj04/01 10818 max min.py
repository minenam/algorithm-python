'''
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

예제 입력 1 
5
20 10 35 30 7

예제 출력 1 
7 35
'''
# 방법1. max, min 함수 활용
N = int(input())
data = list(map(int, input().split()))

# 1-1. 시간은 1-2.보다 빠르나 메모리가 더 필요함
## 메모리: 154060KB | 시간: 408ms
print(min(data), max(data))

# 1-2. 시간은 1-1.보다 다소 느리나 메모리가 덜 필요함
# 메모리: 149432KB | 시간: 424ms
results = [min(data), max(data)]
print(' '.join(map(str, results)))


# 방법2. 1차원 배열 활용하기 - 시간이 방법1보다 느리나 메모리는 1-2.방법과 동일
## 메모리: 149432KB | 시간: 600ms
N = int(input())
data = list(map(int, input().split()))
minNum = data[0]
maxNum = data[0]

for i in range(len(data)):
    # 최솟값 구하기
    if minNum > data[i]:
        minNum = data[i]
    # 최댓값 구하기
    if maxNum < data[i]:
        maxNum = data[i]
   
print(minNum, maxNum)
