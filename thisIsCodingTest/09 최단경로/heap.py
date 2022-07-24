import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for v in iterable:
        heapq.heappush(h, v)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# 내림차순 힙 정렬(Heap Sort)
def heapsort_re(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for v in iterable:
        heapq.heappush(h, -v)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


if __name__ == '__main__':
    result = heapsort([1,2,34,4,235,2,354,2,3,0]) # [0, 1, 2, 2, 2, 3, 4, 34, 235, 354]
    result_r = heapsort_re([1, 2, 34, 4, 235, 2, 354, 2, 3, 0])  # [0, 1, 2, 2, 2, 3, 4, 34, 235, 354]
    print(result)
    print(result_r)
