import os

def listar_arquivos(path='.'):
    for item in os.listdir(path):
        caminho_completo = os.path.join(path, item)
        if os.path.isdir(caminho_completo):
            listar_arquivos(caminho_completo)
        else:
            print(caminho_completo)

listar_arquivos()