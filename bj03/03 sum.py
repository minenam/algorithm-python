'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.

예제)
입력
3

출력
6
'''

n = int(input())

# 풀이1 (반복문)
def Sum(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

print(Sum(n))

# 풀이2 (식)
def Sum2(n):
    return int((n * (n+1)) /2)

print(Sum2(n))
