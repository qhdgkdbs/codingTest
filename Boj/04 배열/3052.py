array = []
result = 0
for _ in range(10):
    val = int(input()) % 42
    if val not in array:
        result += 1
    array.append(val)

print(result)
