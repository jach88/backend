#Condicionales
#If (si) (edad>18).... else ....
edad = int(input("Ingrese la su edad: "))
#si soy de la tercera edad entonces me deben indicar que necesito un tercer refuerzo
if edad > 18 and  edad <= 64 :
    print("Puedes vacunarte")
    print("Sigo en el if")
    print("aiudaaa")
#elif => sino si | siempre va despues de un primer if o despues de otro elif
elif edad >= 65 :
    print("Necesitas tercera dosis")
else:
    print("Todavia no puedes vacunarte")

print("Yo me ejecuto asi se cumpla o no se cumpla el if")


#OPERADOR TERNARIO
#Es una forma de hacer una validacion pero en una sola linea de codigo
#       RESULTADO_IF         IF condicion ELSE       RESULTADO_ELSE
texto = "Eres mayor de edad"if edad >= 18 else "Eres menor de edad"
print(texto)

# variable1, variable2 =["eduardo","martin"]
# print(variable1)
# print(variable2)

#ingresar un numero y validar si es par o impar o 0
numero = int(input("Ingresa el numero: "))

if numero == 0:
    print("El numero es 0")
elif numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

# BUCLES

#FOR => repite desde hasta
meses =['AGOSTO', 'SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
#si nosotros queremos iterar una coleccion de datos la mejor forma es mediante un FOR
for mes in meses:
    print(mes)
#a diferencia del manejo de scopes (alcance) de la variable en JS, en python, la variable sigue existiendo fuera del for
print(mes)
for numero in range(10):
    print(numero)

#el range puede recibir hasta 3 parametros
#range(n) => n: el limite de las iteraciones
#range(m,n) => m: el numero inicial
#range(m,n,o) => o: en cuanto se va a incrementar o decrementar el valos en cada ciclo
for numero in range(5, 10):
    print(numero)

print('===========================')
for numero in range(1, 10, 2):
    print(numero)

# de la siguiente lista de numeros indicar cuantos son positivos y negativos
numeros = [-4,7,-10,8,25,-7]

# hay 3 negativos y 3 positivos
positivos =0
negativos =0
for numero in numeros:
    if(numero >0):
        positivos += 1
    else:
        negativos += 1

print(f"Hay {negativos} negativos y {positivos} positivos")


print("======================================================")
#BREAK
#hace que el bucle finalice de manera inesperada
for segundo in range(60):
    print(segundo)
    if segundo == 10:
        break



