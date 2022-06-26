def solution(N, stages):
    answer = []
    fail = {}

    stages_num = len(stages)

    for i in range(1, N + 1):
        if stages_num <= 0:
            fail[i] = 0
            continue
        fail[i] = stages.count(i) / stages_num
        stages_num -= stages.count(i)

    tmp = sorted(fail.items(), key=lambda x: x[1], reverse=True)
    # sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
    print(tmp)
    return [x[0] for x in tmp]