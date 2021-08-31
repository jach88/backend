from flask import Flask
from conexion_bd import base_de_datos

app = Flask(__name__)
#                                       mysql://username:password@host/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/reposteria_flask'
# si se establece True SqlAlchemy restareará las modificaciones de los objetos (modelos) y lanzará señales de cambio, su valor predeterminado es NONE . igaul habilida el tracking pero emite una advertencia que en futuras versiones se removerá el valor x default None y si o si tendremos que indicar un valor inicial
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#inicia la conexion con la db para darle las credenciales definidas en el app.config
base_de_datos.init_app(app)

#creara las tablas aun no mapeadas y si todo esta bien no devolvera nada
base_de_datos.create_all(app=app)


@app.route("/")
def initial_controller():
    return {
        "message":"Bienvenido a mi API de Reposteria 🥧"
    }

if __name__ == "__main__":
    app.run(debug=True)
