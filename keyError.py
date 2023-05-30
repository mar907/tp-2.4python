diccionario = {'a': 1, 'b': 2, 'c': 3}

try:
    valor = diccionario['d']
    print("Valor:", valor)
except KeyError as error:
    print("Error:", str(error))