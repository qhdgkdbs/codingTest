def self_num(num):
    return num + (num//10) + (num%10)

print()

num = 97

for i in [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]:
    print(i)

while 1:
    num = self_num(num)
    if num > 10000:
        break
    print(num)
