def inverter_string(string):
    if len(string) <= 1:
        return string
    
    return string[-1] + inverter_string(string[:-1])

print(inverter_string("recursao"))
print(inverter_string("python"))
print(inverter_string("abc"))
print(inverter_string("a"))
print(inverter_string(""))
