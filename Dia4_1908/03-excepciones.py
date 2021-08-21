try:
    numero = 5 / 1
    print(f"El numero es {numero}")    #intenta hacer la operacion si no es correcta corre la excepcion
    numero = 1000/ 0

except ZeroDivisionError:
    print("Hubo un error en la division")
except TypeError:
    print("Error de tipo")
except:
    print("Error desconocido")
else:
    print("todo bien")
finally: #finally => no importa si la operacion salio bien o hubo errores, igual se ejecutará
    print("Soy un ejemplo")

#el else para usar el else tenemos que obligatoriamente DECLARAR un except y este se ejecutará cuando no ingresa a ningun except cuando la operacion no tuvo errores

#Ejercicio: ingresar 4 numeros si uno de ellos no es numero entoces no tomarlo en cuenta y volver a pedir hasta que tengamos los 4 numeros

numeros =[]
while len(numeros) != 4:
    try:
        numero = int(input("Ingresa un numero: "))
        numeros.append(numero)
    except:
        pass

print("Los numeros son {}".format(numeros))

