def dividir(dividendo, divisor):
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return dividendo / divisor

try:
    resultado = dividir(27, 0)
    print("El resultado de la división es:", resultado)
except ZeroDivisionError as error:
    print("Error:", str(error))