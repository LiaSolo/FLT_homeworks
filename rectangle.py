

n, m = map(int, input('ВВедите два числа через пробел: ').split())


def rectangle(n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            res += (n - i) * (m - j)
    return res


print(rectangle(n, m))
