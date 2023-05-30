with open("mi_archivo.txt", "a+") as archivo:
    archivo.write("Estoy aprendiendo Python")

# Ejercicio 2: Abrir un archivo, mostrar su estado, modo, nombre y codificación

with open("mi_archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

    print("Estado del archivo:", archivo.closed)
    print("Modo de apertura:", archivo.mode)
    print("Nombre del archivo:", archivo.name)
    print("Codificación de caracteres:", archivo.encoding)
    print("Contenido del archivo:")
    print(contenido)