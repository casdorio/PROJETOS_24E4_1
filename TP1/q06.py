def encontrar_quadrado(quantidade):
    quadrado = 1
    graos = 1

    while graos < quantidade:
        quadrado += 1
        graos *= 2

    return quadrado

print(encontrar_quadrado(16))
print(encontrar_quadrado(1))
print(encontrar_quadrado(64))