from random import *


def miller_rabin_test(n, b, s, t): # 실제 p, q가 소수인지 판별하기 위해 사용한 밀러-라빈 테스트에 대한 함수
    for i in range(b):  # 30번 검증
        a = randint(2, n - 2) # a는 2와 n-2 사이의 정수
        b = pow(a, t, n)  # b = (a^t) % n

        if b == 1 or b == n - 1:
            continue
        for j in range(s - 1):
            b = pow(b, 2, n)  # b = b^2 % n
            if b == n - 1:  # (b % n) = (n - 1) = -1
                break
        else:
            return 0  # composite

    return 1  # probably prime


def is_prime(n):  # p, q가 소수인지 판별하기 위한 함수
    if n == 2:  # n이 2이면 소수, 2가 아닌 짝수이면 홀수
        return 1
    if n % 2 == 0:
        return 0

    b = 30  # 30번 검증

    # (n - 1) = (2 ** s) * t
    t = ((n - 1) // 2)  # n-1을 2로 나눈 나머지가 0이 아닐 때 까지 계속 2로 나눈 값을 저장
    # (n - 1) / 2의 결과는 float 형으로 반환되는데 이럴 경우 n이 너무 크면
    # OverflowError: integer division result too large for a float 에러가 뜨면서 프로그램이 종료되는데
    # t는 정수이고 따라서 float 형으로 반환받지 않아도 되기 때문에 (n - 1) // 2로 하여 결과를 int 형으로 받게 함

    x = t % 2  # t를 2로 나누었을 때 나머지 값을 저장
    s = 1  # s값 초기화

    while x == 0:  # t를 2로 나누었을 때 나머지가 0인 동안 반복
        t = t // 2
        x = t % 2
        s = s + 1

    result = miller_rabin_test(n, b, s, t)
    return result