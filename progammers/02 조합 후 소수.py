import itertools
import math


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(nums):
    result = list(itertools.combinations(nums, 3))
    answer = 0

    for grp in result:
        if is_prime_number(sum(grp)):
            answer += 1

    return answer