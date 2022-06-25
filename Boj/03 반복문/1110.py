new = org = int(input())
front = 0
back = 0

count = 0

while 1:
    if new < 10:
        front = 0
        back = new % 10
    else:
        front = new // 10
        back = new % 10

    new = back * 10 + (front + back) % 10

    count += 1
    if new == org:
        break

print(count)


'''
n = int(input())         # 68
num = n
cnt = 0                  # 사이클 수

while True:              # while 1이랑 동일
    a = num / / 10       # 6
    b = num % 10         # 8
    c = (a + b) % 10     # 6 + 8 = 1"4"
    num = (b * 10) + c   # 80 + 4 = 84

    cnt = cnt + 1        # 사이클 수 + 1
    if(num == n):        # num에서 입력된 n과 똑같은 숫자(68)가 나오면 멈춤
        break

print(cnt)
'''