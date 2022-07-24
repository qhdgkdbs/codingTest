# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              -1: [3, 0], 0: [3, 1], -2: [3, 2]}
    l_roc = keypad[-1]
    r_roc = keypad[-2]

    answer = ''
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l_roc = keypad[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            r_roc = keypad[i]
        else:
            # 더 가까이에 있는 손가락 찾기
            loc = keypad[i]
            l_dist = abs(loc[0] - l_roc[0]) + abs(loc[1] - l_roc[1])
            r_dist = abs(loc[0] - r_roc[0]) + abs(loc[1] - r_roc[1])
            if l_dist == r_dist:
                if hand == 'left':
                    answer += 'L'
                    l_roc = keypad[i]
                else:
                    answer += 'R'
                    r_roc = keypad[i]
            elif l_dist < r_dist:
                answer += 'L'
                l_roc = keypad[i]
            else:
                answer += 'R'
                r_roc = keypad[i]

    return answer