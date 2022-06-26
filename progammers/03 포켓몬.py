# 모법답안
def solution(ls):
    return min(len(ls)/2, len(set(ls)))


# 내가 푼 답안
def solution(nums):
    p_nums = len(nums)//2
    nums = set(nums)

    return len(nums) if len(nums) < p_nums else p_nums
