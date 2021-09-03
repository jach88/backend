from flask_restful import Resource,request, reqparse
import sqlalchemy
from sqlalchemy.orm import session
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.expression import delete
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
        resultado = base_de_datos.session.query(
            IngredienteModel).filter(IngredienteModel.ingredienteId == id).first()

        resultado2 = base_de_datos.session.query(
            IngredienteModel).filter_by(ingredienteId=id).first()
        
        if resultado:
            data = resultado.__dict__
            del data['_sa_instance_state']
            return{
                "message":None,
                "content":data
            }
        else:
            return {
                "message": "El ingrediente no existe",
                "content": resultado
            },404    

    def put(self, id):        
        # ingrediente = base_de_datos.session.query(IngredienteModel).filter(
        #     IngredienteModel.ingredienteId == id).first()
        # if ingrediente is None:
        #     return{
        #         "message":"El ingrediente no existe",
        #         "content": None
        #     }, 404

        # data = serializador.parse_args()
        # print(ingrediente.__dict__)
        # ingrediente.ingredienteNombre = data['nombre']
        # # base_de_datos.session.add(ingrediente)
        # respuesta = ingrediente.__dict__.copy()
        # base_de_datos.session.commit()
        # del respuesta['_sa_instance_state']

        # return{
        #     "message":"El ingrediente existe",
        #     "content": respuesta
        # }
        
        data = serializador.parse_args()
        resultado = base_de_datos.session.query(IngredienteModel).filter(
            IngredienteModel.ingredienteId == id).update(
                {
                    IngredienteModel.ingredienteNombre: data['nombre']
                },synchronize_session='fetch')
        base_de_datos.session.commit()
        if resultado == 0:
            return{
                "message":"No hubo ingrediente a actualizar",
                "content":None
            }, 404
        else:    
            return{
                "message":"El ingrediente fue actualizado exitosamente",
                "content":None
            },204


    def delete(self, id):
        base_de_datos.session.query(IngredienteModel).filter(IngredienteModel.ingredienteId== id).delete()
        base_de_datos.session.commit()
        return{
            "message":"Ingrediente eliminado exitosamente",
            "content":None
        },204
        





serializadorFiltro = reqparse.RequestParser()
serializadorFiltro.add_argument(
    'nombre',
    location='args',
    required=False,
    type=str
)


class FiltroIngredientesController(Resource):
    def get(self):
        filtros = serializadorFiltro.parse_args()
        # resultado=base_de_datos.session.query(IngredienteModel).filter(
        #     IngredienteModel.ingredienteNombre.like('%a%')).all()
        # print(filtros)
        # print(resultado)
        # resultado_final =[]
        # for ingrediente in resultado:
        #     ingrediente_dicc = ingrediente.__dict__.copy()
        #     del ingrediente_dicc['_sa_instance_state']
        #     print(ingrediente_dicc)
        #     resultado_final.append(ingrediente_dicc)
        # return{
        #     "content": resultado_final
        # }

        resultado = base_de_datos.session.query(
            IngredienteModel).filter(IngredienteModel.ingredienteNombre.like('%'+filtros['nombre'] + '%')).with_entities(IngredienteModel.ingredienteNombre, IngredienteModel.ingredienteId).all()
        print(resultado)
        resultado_final =[]
        for registro in resultado:
            resultado_final.append(registro._asdict())
            print(type(registro))
            print(registro._asdict())
        return {
            "content": resultado_final
        }