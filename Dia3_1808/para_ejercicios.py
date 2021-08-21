import random

intentos = 0
numeroIntentos = 6
NumeroMin = 1
NumeroMax = 20

numeroAdivinar = random.randint(NumeroMin,NumeroMax)
print(f"Hola intenta adivinar un numero entre {NumeroMin} y {NumeroMax}")

while intentos < numeroIntentos:
    print("Indicame un numero: ")
    numero = input()
    numero = int(numero)

    intentos = intentos + 1

    if numero < numeroAdivinar:
        print("Tu numero es menor")
    if numero > numeroAdivinar:
        print("Tu numero es mayor")
    if numero == numeroAdivinar:
        break

if numero == numeroAdivinar:
    print("Excelente has adivinado el numero")
if numero != numeroAdivinar:
    print(f"Lo siento el numero era {numeroAdivinar} intentalo nuevamente")