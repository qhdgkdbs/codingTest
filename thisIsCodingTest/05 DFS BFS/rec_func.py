def factorial_rec(i):
    if i == 0:
        return 1
    return i * factorial_rec(i-1)


if __name__ == "__main__":
    print(factorial_rec(5))