'''
문자열이 숫자 길이는 4 or 6, 숫자만 있어야함
'''

import re
def solution(s):
    return (True if s.isdigit() else False) and (len(s) in [4,6])