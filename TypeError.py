def mas_10(numero):
    return numero + 10

def add_10(numero):
    return numero + 10

try:
    resultado = mas_10(5)
    print("Resultado de mas_10():", resultado)
except TypeError as error:
    print("Error:", str(error))

try:
    resultado = add_10("cinco")
    print("Resultado de add_10():", resultado)
except TypeError as error:
    print("Error:", str(error))