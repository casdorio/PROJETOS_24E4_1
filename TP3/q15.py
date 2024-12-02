def contar_repeticoes(string, caractere):
    if not string:
        return 0
    
    return (1 if string[0] == caractere else 0) + contar_repeticoes(string[1:], caractere)

print(contar_repeticoes("banana", "a"))
print(contar_repeticoes("abacaxi", "x"))
print(contar_repeticoes("hello world", "o"))
print(contar_repeticoes("teste", "z"))
print(contar_repeticoes("", "a"))
