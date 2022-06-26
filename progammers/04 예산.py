'''
입출력 예
d	budget	result
[1,3,2,5,4]	9	3
[2,2,3,3]	10	4
'''

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        print(d)
        d.pop()
    return len(d)