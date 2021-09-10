from flask import Flask
from flask_restful import Api
from config.conexion_bd import base_de_datos
from models.Tarea import TareaModel
from controllers.Usuario import RegistroController, LoginController

from dotenv import load_dotenv   #para buscar el archivo .env
from os import environ

load_dotenv()

app = Flask(__name__)
api = Api(app)


#son las variables de configuracion de mi proyecto flask DEBUG=TRUE, PORT=500, ENVIROMENT=DEVELOPMENT
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

base_de_datos.init_app(app)
base_de_datos.create_all(app=app)


api.add_resource(RegistroController,'/registro')
api.add_resource(LoginController,'/login')

if __name__ == '__main__':
    app.run(debug=True)