# 그래프 탐색 알고리즘 : DFS / BFS
* 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정


### 스택 자료구조
* 먼저 들어온 데이터가 나중에 나가는 구조
<pre><code>stack = []
stack.append(5)
stack.append(10)
stack.pop()       #10
</code></pre>
* 최상단 원소부터 출력
```stack[::-1]    # 10 5```
* 최하단 원소부터 출력
```stack          # 5 10 ```


### 큐 자료구조
* 선입선출, 대기열 같은 녀석
* 리스트로도 구현은 가능하지만, 속도 측면에서 deque가 훨씬 유리
<pre><code>from collections import deque

queue = deque()

queue.append(5)
queue.append(10)
queue.popleft()       #5
</code></pre>
* 먼저 들어온 순서대로 출력
```queue    # 5 10```
* 나중에 들어온 원소부터 출력
```queue.reverse()     # 10 5 ```
* 