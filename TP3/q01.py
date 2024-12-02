import os

def explorar_pasta(caminho, nivel=0):
    try:
        itens = os.listdir(caminho)
        for item in itens:
            caminho_completo = os.path.join(caminho, item)

            if os.path.isdir(caminho_completo):
                print(f"{'  ' * nivel}[D] {item}")
                explorar_pasta(caminho_completo, nivel + 1)
            else:
                print(f"{'  ' * nivel}[F] {item}")
    except PermissionError:
        print(f"{'  ' * nivel}[!] Permissão negada para acessar: {caminho}")
    except FileNotFoundError:
        print(f"{'  ' * nivel}[!] Caminho não encontrado: {caminho}")
    except Exception as erro:
        print(f"{'  ' * nivel}[!] Ocorreu um erro: {erro}")

caminho_diretorio = input("Informe o caminho da pasta para explorar: ")
if os.path.exists(caminho_diretorio) and os.path.isdir(caminho_diretorio):
    print(f"Explorando o diretório '{caminho_diretorio}':")
    explorar_pasta(caminho_diretorio)
else:
    print("O caminho fornecido não é um diretório válido.")
