'''
문제
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

예제 입력 1 
ljes=njak
예제 출력 1 
6
'''

# 입력 
strings = input()

# 내 풀이
def my_solution(strings):
    croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 변경된 크로아티아 알파벳
    texts = list() # 입력 문자열을 한 글자씩 나눠 담을 리스트
    count_croa = 0 # 변경된 크로아티아 알파벳 개수
    len_croa = 0   # 변경된 크로아티아 알파벳 단어 총 길이
    croa = list()  
    words = str() 
    answer = 0
    
    
    # 입력 받은 문자열을 한 글자씩 나눠 리스트 형태로 저장
    for string in strings:
        texts.append(string)
    
    for i in range(len(texts)):
        # 맨 앞부터 각 글자를 하나씩 붙여나가면서
        words += texts[i]
        # 변경된 크로아티아 알파벳 단어와 같은지 확인
        for croatia in croatia_list:
            if words.__contains__(croatia):
                # 변경된 크로아티아 알파벳 개수 카운팅
                count_croa += 1
                # 변경된 크로아티아 알파벳 별도로 리스트에 저장
                croa.append(croatia)
                words = str()
    
    # 변경된 크로아티아 알파벳 단어 총 길이 저장
    for c in croa:
        len_croa += len(c)

    # 정답 = 전체 문자열 길이 - 변경된 크로아티아 알파벳 총 길이 + 변경된 크로아티아 알파벳 단어 개수
    answer = (len(strings) - len_croa) + count_croa

    return answer


# 풀이1. count() 활용 https://data-analysis-expertise.tistory.com/95
## 시간: 72ms
def solution1(strings):
    croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 변경된 크로아티아 알파벳
    count_croa = 0

    # 각 알파벳 단어마다 돌면서
    for croatia in croatia_list:
        # 입력 문자열에 포함되면
        if croatia in strings:
            # count()함수로 개수를 카운팅 한다
            count_croa += strings.count(croatia)

    # count_croa 를 두 번 곱한 것을 빼고 다시 더하는 이유는 "dz="과 "z="이 중복으로 카운팅된다.
    answer = len(strings) - count_croa * 2 + count_croa
    return answer

# 풀이2. replace 활용 https://velog.io/@myway00/092
## 시간: 80ms
def solution2(strings):
    croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 변경된 크로아티아 알파벳
    for croatia in croatia_list:
        strings = strings.replace(croatia, ' ')
    return len(strings)

print(solution1(strings))
# print(solution2(strings))