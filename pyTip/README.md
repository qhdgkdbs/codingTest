# 파이썬 정리

* map함수
  * map(function, iterable) -> list 혹은 tuple로 형 변환하여 사용
    * ```list(map(lambda n: n+1, [1, 2, 3]))```
* Truthy 값과 Falsy 값
  * Falsy 값
    * False 
    * None 
    * 0, 0.0, 0L, 0j 
    * "" 
    * [] 
    * () 
    * {}
  * Truthy 값
    * 기본 OBJ 중 위의 F값 제외 전부


## 유용한 표준 라이브러리
  * 내장 함수
    * 기본
      * ```sum([1,2,3,4,5])```
      * ```max(1,2,3,4) max(12,3,31,3,1)```
      * ```eval("(3+5)*7")```
    * 정렬
      * ```result = sorted([1,3,42,1,3], reverse = true) #기본값은 오름차순, reverse -> 내림차순```
      * ```arr = [('홍길동', 35), ('이순신', 75), ('아무개, 50)] result = sorted([1,3,42,1,3], key=lambda x: x[1])```
  * itertools
    * 순열과 조합
      * 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
        * <pre><code>from itertools import permutations 
          data = ['A', 'B', 'C']
          result = list(permutations(data, 3)) # 모든 순열 구하기
          print(result) 
          # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
          </code></pre>
      * 중복 순열 :
        * <pre><code>from itertools import product 
          data = ['A', 'B', 'C']
          result = list(product(data, repeat = 2))
          print(result) 
          # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
          </code></pre>
    
      * 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
        * <pre><code>from itertools import combinations 
          data = ['A', 'B', 'C']
          result = list(combinations(data, 2)) # 모든 순열 구하기
          print(result) 
          # [('A', 'B'), ('A', 'C'), ('B', 'C')]
          </code></pre>
      * 중복 조합 : 
        * <pre><code>from itertools import combinations_with_replacement 
          data = ['A', 'B', 'C']
          result = list(combinations_with_replacement(data, 2)) # 모든 순열 구하기
          print(result) 
          # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
          </code></pre>
  * heapq : 힙 자료구조
    * 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
  * bisect : 이진 탐색 
  * collections : 덱, 카운터 등의 유용한 자료구조
    * Counter : iter 가능한 구조에서 몇번 나오는지
        <pre><code>from collections import Counter
      counter = Counter(['red', 'blue', 'red', 'green'])
      print(counter['blue'])
      print(counter['green'])
      print(counter['gre'])
      print(dict(counter)) # {'red': 2, 'blue': 1, 'green': 1}</code></pre>
  
  * math : 수학적
    * 팩토리얼 제곱근 GCD 삼각함수 등
      * <pre><code>import math 
        def lcm(a,b) : #최소공배수
          return a*b / match.gcd(a,b)
        math.gcd(21, 14) #7
        lcm(21, 14) #42</code></pre>

### 파이썬 자료형 변환
  1. 파이썬 정수 변환 - int()
  2. 파이썬 실수 변환 - float()
  3. 파이썬 문자열 변환 - str()
  4. 파이썬 문자 변환 - chr()
  5. 파이썬 불리언 변환 - bool()

### 아스키 코드 변환 관련
* ord 함수 <br/>
```col = int(ord(loc[0])) - int(ord('a')) + 1```
* chr 함수 <br/>
```chr(97) # a```

### 파이썬 문자열/숫자 확인 함수
```"hello".isalpha()``` <br/>
```"0123".isdigit()``` <br/>
```"0sdf0df".isalnum() # 문자 또는 숫자```


### global 선언자
* 함수 안에서 전역 변수 변경하기
<pre><code>
x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
</code></pre>

* 함수 안에서 global을 사용하면 해당 변수는 전역 변수가 됨.
<pre><code>
# 전역 변수 x가 없는 상태
def foo():
    global x    # x를 전역 변수로 만듦
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
</code></pre>



<pre><code>

</code></pre>