arr = [1,3,1,5]
val = [0] * len(arr)

val[0] = arr[0]
val[1] = max(arr[0], arr[1])

for i in range(2,len(arr)):
    val[i] = max(val[i - 2] + arr[i], val[i-1])

print(val[-1])