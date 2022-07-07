def solution(n):
    return int(''.join(sorted([*str(n)], key = lambda x: int(x), reverse = True)))