def inverter_fila(fila):
    fila_invertida = []
    while fila:
        fila_invertida.append(fila.pop())
    return fila_invertida


fila_pacientes = ["Maria", "João", "Pedro", "Ana", "Carlos"]

print("Fila original:", fila_pacientes)

fila_invertida = inverter_fila(fila_pacientes)

print("Fila invertida:", fila_invertida)