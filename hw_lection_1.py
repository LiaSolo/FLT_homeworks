
def find_n(k):
    n = 0
    while (n + 1) * (n + 2) / 2 < k:
        n += 1
    print(n)
    return n


def J(k):
    n = find_n(k)
    N = n * (n + 1) / 2
    return int(k - N)


def I(k):
    n = find_n(k)
    j = J(k)
    return int(n - j + 2)


k = 10
print(I(k), J(k))
