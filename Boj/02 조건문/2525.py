t, m = list(map(int, input().split()))
added = int(input())

time_m = t*60 + m
time_m += added

if time_m//60 >= 24:
    print(time_m//60 - 24, time_m%60)
else:
    print(time_m//60, time_m%60)