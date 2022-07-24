# others
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


# 나의 풀이
def nary(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    return rev_base


def solution(n):
    answer = 0
    answer = int(nary(n, 3), 3)
    return answer