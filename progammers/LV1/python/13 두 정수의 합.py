def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a, b+1))

print(adder(3, 5))