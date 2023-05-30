tupla = (3, 8, 2, 9, 6, 4, 7)
cantidad = len(tuple(filter(lambda x: x > 5, tupla)))
print(cantidad)