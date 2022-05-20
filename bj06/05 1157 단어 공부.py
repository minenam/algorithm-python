'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
'''
# 입력함수
input_word = input()

# 풀이1. 리스트 여러 번 생성
def solution1(input):
    # 인자로 받은 입력단어를 대문자로 일괄 변환한다. (대소문자 구분하지 않음)
    answer = ''
    word = input.upper()
    # 소문자로된 입력단어를 알파벳 하나씩 돌아가며, 각 알파벳당 빈도수를 계산한다.
    count_alpha = dict()
    for alpha in word:
        if alpha not in count_alpha:
            count_alpha[alpha] = 1
        else:
            count_alpha[alpha] += 1
    # 빈도수가 가장 큰 알파벳을 반환한다.
    max_value = max(count_alpha.values())
    count = 0
    for alpha, value in count_alpha.items():
        if max_value == value:
            count += 1
            answer = alpha
    # 만약 빈도수가 최대인 알파벳이 여러 개면 '?'를 반환한다.
    if count > 1:
        answer = '?'
    return answer


print(solution1(input_word))

