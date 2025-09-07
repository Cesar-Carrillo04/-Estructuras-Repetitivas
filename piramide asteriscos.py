alt = int(input("Introduce la altura de la piramide: "))

for i in range (1, alt + 1):
    esp = " " * (alt - i)
    aste = "*" * (2 * i - 1)
    print(esp + aste)
