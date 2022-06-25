array = [0]*10
mul = 1
for _ in range(0, 3):
    mul *= int(input())

for j in str(mul):
    array[int(j)] += 1

for i in array:
    print(i)