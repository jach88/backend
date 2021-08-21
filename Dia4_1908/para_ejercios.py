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

print("=============================================================")

#