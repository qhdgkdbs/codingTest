
### **파일 입, 출력**
* 파일에서 입력받기
<pre><code># input.txt 안에 입력값 저장
import sys
sys.stdin = open("input.txt", 'r')
string = input()
</code></pre>

* 숫자 입력 나눠서 받기
<pre><code># 6 3
N, M = map(int, input().split())
</code></pre>

* 숫자 입력 한꺼번에 받기
<pre><code># 2 3 5 7 9 11
nums = list(map(int, input().split())
</code></pre>

* 2차원 배열 받기
<pre><code>'''
9 8 3 1
5 2 4 7
2 3 5 6
5 2 3 4
'''
maze = [list(map(int, input().split())) for _ in range(4)]
</code></pre>


* 2차원 배열 예쁘게 출력하기
<pre><code>arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(*arr, sep='\n')
'''
1 2 3
4 5 6
7 8 9
'''
</code></pre>

### **자료구조**
* 큐
<pre><code>from collections import deque
q = deque()
q.append(2)
print(q.popleft())  # 2
</code></pre>

* 최소 힙
<pre><code>import heapq
q = []
heapq.heappush(q, (1, 'apple'))
print(heapq.heappop(q)[1])    # 'apple'
</code></pre>

### 유틸리티
* 문자 to ASCII
<pre><code>print(ord('a'))    # 97
</code></pre>

### 순열과 조합
* 배열로 순열 생성
<pre><code>from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)   # [('A', 'B', 'C'), ('A', 'C', 'B'), ..., ('C', 'B', 'A')]
</code></pre>

* 배열로 조합 생성
<pre><code>from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)   # [('A', 'B'), ('A', 'C'), ('B', 'C')]
</code></pre>

* 배열로 중복 순열 생성
<pre><code>from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)   # [('A', 'A'), ('A', 'B'), ..., ('C', 'C')]
</code></pre>

### 기타 테크닉
* list comprehension을 사용한 리스트 값 필터링
<pre><code>arr = [7, 1, 2, 5, 4, 2, 0]
pivot = 3
left_side = [x for x in arr if x <= pivot]
print(left_side)    # [1, 2, 2, 0]
</code></pre>

* 튜플 리스트 정렬
<pre><code>arr = [('apple', 17), ('banana', 8), ('candy', 3)]
arr.sort(key=lambda x: x[1])
print(arr)    # [('candy', 3), ('banana', 8), ('apple', 17)]
</code></pre>

* for 반복문 인덱스 가져오기
<pre><code>arr = ['a', 'b', 'c']
for i, char in enumerate(arr):
    print(f'{i}: {char} ', end='')   # 0: a 1: b 2: c 
</code></pre>

* 두 배열로 튜플로 묶기
<pre><code>numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair, end='')     # (1, 'A')(2, 'B')(3, 'C')
</code></pre>

* 이진 탐색
<pre><code>from bisect import bisect_left, bisect_right
numbers = [1, 4, 6, 8, 11, 19]
target = 11
print(bisect_left(numbers, target))     # 4
print(bisect_right(numbers, target))     # 5
</code></pre>