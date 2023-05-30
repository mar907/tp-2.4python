archivo = open("mi_archivo.txt", "r", encoding="utf-8")
contenido = archivo.read()

print("Estado del archivo:", archivo.closed)
print("Modo de apertura:", archivo.mode)
print("Nombre del archivo:", archivo.name)
print("Codificación de caracteres:", archivo.encoding)
print("Contenido del archivo:")
print(contenido)

archivo.close()
