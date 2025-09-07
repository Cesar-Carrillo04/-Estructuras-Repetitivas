print("Contador de dígitos")
numero = input("Introduce un número entero: ")

contador = 0
for caracter in numero:
    if caracter.isdigit():
        contador += 1

print(f"El número tiene {contador} dígito(s).")
