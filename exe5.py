palavra = 'banana'

def inverter_string(palavra):
    return palavra[::-1]

def inverter_string_while(palavra):
    string_invertida = ""
    index = len(palavra) - 1
    while index >= 0:
        string_invertida += palavra[index]
        index -= 1
    return string_invertida

print(inverter_string(palavra))
print(inverter_string_while(palavra))
