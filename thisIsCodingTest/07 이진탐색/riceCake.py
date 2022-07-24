import time

def rice_cake(cnt, min_len, rice):
    r_arr = list(map(int, rice.split()))

    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(r_arr)

    # 이진 탐색 반복 수행(반복적)
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in r_arr:
            # 잘랐을 때의 떡의 양 계산
            if x > mid:
                total += x - mid
        # 떡의 양이 부족한 경우
        if total < min_len:
            # 떡을 더 짤라야하니깐, end 를 줄여버려
            end = mid - 1
        else:
            # 떡의 길이가 충분하니깐, start(높이)를 키워버려
            result = mid
            start = mid + 1

    return result


def answer_rice_cake(cnt, min_len, rice):
    pass

if __name__ == '__main__':
    start = time.time()
    print(rice_cake(4, 6, '19 15 10 17'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    answer_rice_cake(4, 6, '19 15 10 17')
    print(f"{time.time() - start:.10f} sec")


