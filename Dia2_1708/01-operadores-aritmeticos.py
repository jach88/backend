numero1 = 10
numero2 = 80

persona1 = "Eduardo"
persona2 = "Ricardo"

#suma: Si las dos o mas variables son numericas entonces se realizará la suma, si por el contrario las variables son string (caracteres) se CONCATENARAN em el caso de JS si se puede sumar diferentes tipos de variable en el caso de python eso no está permitido 
print(numero1+numero2)
print(persona1+persona2)
numero1_string = str(numero1)
print(numero1_string + persona1)
#resta
#No se puede usar la resta en variables que no sean numericas
#print(persona1 - persona2)

print(numero1 - numero2)

#multiplicacion
print(numero1 * numero2)
#la multiplicacion de 10 y 80 es:800
print("La multiplicacion de {} y {} es:{}".format(numero1,numero2,numero1*numero2))
print("La multiplicacion de {0} y {1} es:{2}".format(numero1,numero2,numero1*numero2))
print(f"La multiplicacion de {numero1} y {numero2} es:{numero1*numero2}")

#division: Toda division aun asi sea entera siempre será flotante( tiene una parte entera y una parte decimal) 
print(numero2/numero1)
print(numero1/numero2)

#modulo
#el modulo es el resultado de la division
print(numero2 % numero1)
print(numero1 % numero2)

#cociente
#
print(numero2 // numero1)
print(numero1 // numero2)



