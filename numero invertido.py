print("Número invertido")
numero = int(input("Introduce un número entero: "))

invertido = 0
original = abs(numero)

while original > 0:
    digito = original % 10
    invertido = invertido * 10 + digito
    original //= 10

if numero < 0:
    invertido = -invertido

print(f"Número invertido: {invertido}")
