num= int(input("Introduce un numero entero positivo: "))
sumpar = 0
sumimp = 0

for i in range (1, num +1):
    if i%2 ==0:
        sumpar += i
    else:
        sumimp += i
print("suma de pares: " ,sumpar)
print("suma de impares: " ,sumimp)
