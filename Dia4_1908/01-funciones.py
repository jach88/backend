#una funcion es un bloque de codigo que se va a ejecutar cuantas veces sea llamada la funcion

#primero se ejecuta el print luego realiza el print llamar y se ejecuta el saludar luego recien se muestra la funcion

print ("buenas tardes")  #1

def saludar():
   print("Hola buenas tardes")  #3

print("buenas noches") #2
saludar()   

#funciones con parametros
#los parametros que usan las funciones o las variables creadas dentro de las mismas solamente podran ser accedidas dentro de ellas

def saludarPersona(nombre):
    edad = 40
    print(f"Hola {nombre} como te va")

saludarPersona("Christian")

def sin_nombre():
    """Funcion quen o hace nada y solamente es de muestra"""
    print("Yo soy una funcion sin nombre")

sin_nombre()

#las funciones pueden recibir parametros y estos pueden ser opcionales
def registro(nombre, correo=None):
    print("Registro existoso")

registro("Christian")
registro("Eduardo", "ederiveroman@gmail.com")
# registro() la funcion no puede ser vacia porque se tiene el campo nombre oblicatorio

# Crear una funcion llamada identificacion en la cual se reciba el nombre, apellido y la nacionalidad del cliente, si en el caso no se pasa la nacionalidad entonces sera Peruano, imprimir el resultado en forma de un diccionario
def identificacion(nombre,apellido,nacionalidad="Peruano"):
    resultado ={
        "nombre":nombre,
        "apellido":apellido,
        "nacionalidad":nacionalidad
    }
    print(resultado)

identificacion("Christian", "Julca","Peruano")

#todos los parametros que tengan un valor predeterminado SIEMPRE van al final
def sumatoria(num1,num2=10,num3=15):
    print(num1+num2+num3)

sumatoria(10)

#el parametro que tiene el simbolo * es un parametro especial de python que sirve para almacenar n valores
#todos los valores que pasemos a ese parametro se almacenan en una tupla en el mismo orden con el cual hemos pasado los parametros
def alumnos(*args):  #args es igual a argumentos
    print(args)

alumnos(
    "Eduardo",
    "Siannet"
    "Pablo",
    "Fernando",
    "Rick",
    "Jonathan")

def tareas(nombre, apellido, *args ):
    print("ok")

tareas("Eduardo","martinez","1","2",3)  #eduardo pertenece a nombre// 123 pertenece a arg //y el apellido se asigna



def alumnos():
    #implementar logica
    pass     #se usa cuando todavia no definiremos algo en una funcion y queremos passarlo

x=5


#en la funcion alumnos notas se recibira una cantidad n de alumnos en la cual se debe indicar cuantos aprobarion y cuantos desaprobaron siendo la nota minima 11

def alumnos_notas(*args):
    aprobados= 0
    desaprobados= 0
    for alumno in args:
        if alumno['promedio'] >10:
            aprobados +=1
        else:
            desaprobados +=1
    print(
        f"Hay {aprobados} alumnos aprobados y {desaprobados} alumnos desaprobados"
    )
        

    # print(args)    

alumnos_notas(
    {"nombre":"Raul", "promedio": 17},
    {"nombre":"Roxana", "promedio": 20},
    {"nombre":"Alfonso", "promedio": 10},
    {"nombre":"Pedro", "promedio": 8},
    {"nombre":"Katherine", "promedio": 16}
)

alumnos_notas

#keyword arguments => es muy similar a los *args solo con la diferencia que los kwargs usan el nombre del parametro (nombre="Eduardo")
def indeterninada(**kwargs):
    print(kwargs)

indeterninada(nombre="eduardo", apellido="de rivero", nacionalidad="Peruano")
indeterninada(edad=50,estatura=2.10)

def variada(*args, **kwargs):
    print(args)
    print(kwargs)

variada(10, "Eduardo",{"est_civil":"Viudo"},
        mascota="Firulais", raza="Buldogs")



def sumatoria(num1,num2):
    return num1+num2
    print("otra cosa")

rpta = sumatoria(10,5)