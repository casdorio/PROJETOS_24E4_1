def verificar_duplicatas(lista):
    elementos_vistos = {} 
    
    for item in lista:
        if item in elementos_vistos:
            return True
        else:
            elementos_vistos[item] = True
    
    return False

lista = [1, 2, 3, 4, 5, 6, 2]
resultado = verificar_duplicatas(lista)
if resultado:
    print("A lista contém duplicatas.")
else:
    print("A lista não contém duplicatas.")
