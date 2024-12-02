def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    
    if palavra[0] != palavra[-1]:
        return False
    
    return eh_palindromo(palavra[1:-1])

palavra1 = "radar"
palavra2 = "python"
palavra3 = "ana"
palavra4 = "arara"

print(f"A palavra '{palavra1}' é um palíndromo? {eh_palindromo(palavra1)}")
print(f"A palavra '{palavra2}' é um palíndromo? {eh_palindromo(palavra2)}")
print(f"A palavra '{palavra3}' é um palíndromo? {eh_palindromo(palavra3)}")
print(f"A palavra '{palavra4}' é um palíndromo? {eh_palindromo(palavra4)}")
