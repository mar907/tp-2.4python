lista = [1, 2, 3, 4, 5]

try:
    index = 0
    while True:
        elemento = lista[index]
        print("Elemento en el índice", index, ":", elemento)
        index += 1
except IndexError as error:
    print("Error:", str(error))