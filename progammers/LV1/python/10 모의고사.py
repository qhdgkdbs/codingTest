def solution(answers):
    answer = []

    user1 = [1, 2, 3, 4, 5]  # 5
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    s1, s2, s3 = 0, 0, 0

    for idx, ans in enumerate(answers):
        if ans == user1[idx % 5]:
            s1 += 1
        if ans == user2[idx % 8]:
            s2 += 1
        if ans == user3[idx % 10]:
            s3 += 1

    s_max = max(s1, s2, s3)

    if s_max == s1:
        answer.append(1)
    if s_max == s2:
        answer.append(2)
    if s_max == s3:
        answer.append(3)

    return answer