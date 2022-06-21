def rec_func(i):
    if i == 10:
        return
    print(f'{i} 번째 함수에서 {i + 1}재귀 함수를 호출합니다')
    rec_func(i+1)
    print(f'{i} 번째 함수가 종료되었습니다.')


if __name__ == "__main__":
    print(rec_func(1))