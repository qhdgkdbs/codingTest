# 모법답안
# 저도 몰라서 찾아봤는데 i**0.5는 i의 제곱근을 구하는 식이라네요. 4의 제곱근은 2고 25의 제곱근은 5이듯이요.
# 근데 이 제곱근이 정수로 표현이 가능한 수는 약수의 개수가 홀수개 랍니다.
# 2를 제곱근으로 가지는 4는 1,2,4 이렇게 3개, 5를 제곱근으로 가지는 25는 1,5,25 로 3개입니다.
# 반면 10의 제곱근은 3.1622776601683795 으로 정수가 아닌데 10의 약수는 1,2,5,10 이렇게 4개로 짝수이죠.
# 그래서 제곱근에 int를 씌운 것과 안씌운 것이 동일한지 아닌지 판단하는거라고 합니다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer



# 나의 풀이
def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                # 약수의 개수
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer