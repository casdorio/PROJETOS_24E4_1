def funcao1(n):
    for i in range(n):
        print(i)


def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)