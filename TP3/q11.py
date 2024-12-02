import sys

sys.set_int_max_str_digits(50000)

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

def fatorial_cauda(x, acumulador=1):
    if x == 0:
        return acumulador
    return fatorial_cauda(x - 1, acumulador * x)

def fatorial_iterativo(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado

numero = 10000

try:
    print("Fatorial (recursivo):", fatorial(numero))
except RecursionError:
    print("Erro: Fatorial recursivo falhou devido ao limite de profundidade.")

try:
    print("Fatorial (recursão de cauda):", fatorial_cauda(numero))
except RecursionError:
    print("Erro: Fatorial com recursão de cauda falhou devido ao limite de profundidade.")

try:
    print("Fatorial (iterativo): Funcionando, tamanho do resultado =", len(str(fatorial_iterativo(numero))), "dígitos")
except Exception as e:
    print("Erro na função iterativa:", e)
