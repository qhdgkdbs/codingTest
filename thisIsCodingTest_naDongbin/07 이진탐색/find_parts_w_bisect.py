from bisect import bisect_left

mart = int(input())
m_list = list(map(int, input().split()))

customer = int(input())
c_list = list(map(int, input().split()))

m_list.sort()

def binsearch(l,e):
    index = bisect_left(l, e)
    if index == len(l) or l[index] != e:
        return False
    return index


for find in c_list:
    if binsearch(m_list, find):
        print('yes')
    else:
        print('no')


'''
5
8 3 7 9 2
3
5 7 9
'''