from flask_restful import Resource,request, reqparse
import sqlalchemy
from sqlalchemy.sql.elements import True_
from models.ingrediente import IngredienteModel
from models.log import LogModel
from conexion_bd import base_de_datos

#serializador => elemento que convierte los parametros que me envia el front para tener un uso correcto en el backend
serializador = reqparse.RequestParser()
serializador.add_argument(
    'nombre', # nombre del argumento que esperará ser recibido
    required=True, # indica si el argumento es requerido o no lo es
    location='json', #indica la ubicación por donde se deberá proveer el argumento
    help='Falta el nombre', # mensaje si es que es requerido y no es proveido
    type=str, #tipo de dato que se tiene que enviar en el front
)

class IngredientesController(Resource):
    def get(self):
        ingredientes = base_de_datos.session.query(IngredienteModel).all()
        print(ingredientes)
        resultado = []
        for ingrediente in ingredientes:
            print(ingrediente)   
            print(ingrediente.__dict__)
            ingrediente_dicc = ingrediente.__dict__
            del ingrediente_dicc['_sa_instance_state']
            resultado.append(ingrediente_dicc)        
        print("Ingreso al get")
        return{
            "message": None,
            "content":resultado
        }
    
    def post(self):
        #validar en base a los argumentos indicados si esta cumpliendo o no el front con pasar dicha informacion
        data = serializador.parse_args()
        try:
            nuevoIngrediente = IngredienteModel(ingredienteNombre=data['nombre'])
            base_de_datos.session.add(nuevoIngrediente)
            base_de_datos.session.commit()
            # print(nuevoIngrediente.__dict__)
            json ={
                "id":nuevoIngrediente.ingredienteId,
                "nombre": nuevoIngrediente.ingredienteNombre
            }
            error = None
            return {
                "message":"Ingrediente creado exitosamente",
                "content":json
            }, 201
        except sqlalchemy.exc.DataError as err:
            error = err        
            return {
                "message":"Error al ingresar el ingrediente"
            },500
        except sqlalchemy.exc.IntegrityError as err:
            error = err
            return{
                "message":"Ese ingrediente ya existe"
            },500
        
        except Exception as err:
            error = err
            print(err)
            return{
                "message":"Error desconocido"
            },500

        finally:
            #se va a ejecutar si ingreso o no ingreso algun except
            print('Ingreso al finally')
            if error is not None:
                base_de_datos.session.rollback()
                nuevoLog = LogModel()
                nuevoLog.logRazon = str(error)
                base_de_datos.session.add(nuevoLog)
                base_de_datos.session.commit()

    

class IngredienteController(Resource):
    def get(self,id):
        resultado1 = base_de_datos.session.query(
            IngredienteModel).filter(IngredienteModel.ingredienteId == id).first()

        resultado2 = base_de_datos.session.query(
            IngredienteModel).filter_by(ingredienteId=id).first()
        
        print(resultado1)
        print(resultado2)
        return {
            "message": id
        }    

    def put(self):
        pass

    def delete(self):
        pass
