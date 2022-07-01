import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)

    while q:
        low1 = heapq.heappop(q)
        low2 = heapq.heappop(q)
        if low1 >= K:
            return answer

        heapq.heappush(q, low1 + (low2 * 2))
        answer += 1

        # 길이가 0 이거나 1인 경우
        if len(q) == 0:
            return -1
        elif len(q) == 1:
            return -1 if q[0] < K else 1
    return -1


if __name__ == '__main__':
    solution([1, 2, 3, 9, 10, 12], 7)