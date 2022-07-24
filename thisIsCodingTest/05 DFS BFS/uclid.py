def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 6 리턴
# gcd(12, 6) 6 리턴
# gcd(30, 12) 6 리턴
# gcd(162, 30) 6 리턴
# gcd(192, 162) 6 리턴


if __name__ == '__main__':
    print(gcd(192, 162))