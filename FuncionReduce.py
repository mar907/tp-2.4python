from functools import reduce

tupla = (3, 8, 2, 9, 6, 4, 7)
cantidad = reduce(lambda acc, x: acc + 1 if x > 5 else acc, tupla, 0)
print(cantidad)