#list => listas
#ordenadas, y , modificables
colores =['morado','azul','rosado','amarillo']
mezclada=['otoño',14,False,15.2,[1,2,3]]

#imprimir la primera posicion
# en python si la posicion no existe, lanzara un error, a diferencia de JS que indicará undefined(no definido)
print(colores[0])
#al usar valores negativos en las posiciones de la lista, se invertira y podremos recorrer dicha lista
print(colores[-1])
print(colores[1:2])  #lashasta la posicion < que 2
print(colores[1:3])  #las posiciones que sean desde la 1 hasta la posicion < que 3 
print(colores[:3])  #toda la lista hasta la posicion < 2 
print(colores[:2]) #sirve para copiar el contenido de la lista mas no su ubicacion de memoria
colores_2 = colores[:]
print(id(colores_2))
print(id(colores))

print(colores[1:-1])

#metodo para agregar un elemento a una lista
colores.append('naranja')
print(colores)

#metodo para eliminar un valor
#1._solamente si existe lo eliminara, sino lanzará un error
colores.remove('azul')
print(colores)
# colores.remove('azul')
# print(colores)

#2.- si queremos eliminarlo y ademas guardar el valor eliminado en una varianble
color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

#3. el metodo para eliminar el valor
#este metodo tambien sirve para eliminar variables
# nombre="Christian"
# del nombre
# print(nombre)

del colores[0]
print(colores)
