'''
문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

예제 입력 1 
1
2
3
4
5
6
7
8
9
10
- 각 수를 42로 나눈 나머지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 10이다.

예제 출력 1 
10
'''

import sys

def inputNum():
    inputs = []
    for i in range(10):
        inputs.append(int(sys.stdin.readline().rstrip()))
    return inputs

def modNum(numbers):
    mods = []
    for i in range(len(numbers)):
        if mods.count(numbers[i]) > 2:
            mods.remove(numbers[i])
        mods.append(numbers[i] % 42)
    count = len(set(mods))
    return count
 
print(modNum(inputNum()))