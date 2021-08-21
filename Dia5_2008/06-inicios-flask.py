from flask import Flask

#__name__ => muestra si el archivo en el cual se esta llamdando a la clase Flask es el archivo principal del proyecto, esto hace que la instancia de la clase Flask se pueda crear en otros lados (patron de diseño Singletton)
app = Flask(__name__)

#si estamos en el archivo principal del proyecto nos imprimirá __main__ caso contrario la ubicacion del archivo
#print(__name__)

# @ decorador => es un patron de software que se ultiza para modificar el funcionamiento de una clase o una funcion en particular sin la necesidad de emplear otros metodos como la herencia ( cosa que no se puede en una funcion comun y corriente)

@app.route('/')
def inicio():
    print("Me llamaron!")
    return {
        "message": "Hello World!"
    }
    
    
#NOTA: Todo el codigo a implementar siempre debe estar antes del metodo run()
app.run(debug=True)