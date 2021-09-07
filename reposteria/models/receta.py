from conexion_bd import base_de_datos
from sqlalchemy import Column, types, orm
from enum import Enum


class EnumPorcion(Enum):
    personal = "personal"
    familiar = "familiar"
    mediano = "mediano"

    
class RecetaModel(base_de_datos.Model):
    __tablename__ ="recetas"

    recetaId = Column(type_=types.Integer, name="id",
                      primary_key=True, autoincrement=True, unique=True)
    
    recetaNombre = Column(
        name='nombre', type_=types.String(length=255), nullable=False)

    recetaPorcion = Column(name='porcion',type_=types.Enum(EnumPorcion))

    # el argumento en orm realationship es el nombre del modelo no de la tabla
    #el relationship sirve para indicar los hijos que puede tener ese modelo con alguntas realaciones previamente declaradas
    #backref => crea un atributo virtual en el otro modelo y sirve para que se pueda acceder a todo el objeto inverso
    #lazy => define como SQLAlquemy va a cargar la informacion adyacente de la base de datos
    #True / 'select' => carga toda la informacion siempre
    #False / 'joined  => solamente cargara cuando sea necesario (cuando se vaya a usar los atributos auxiliares)
    #'subquery' => trabajará con todos los datos pero en forma de una sub consulta
    #'dynamic' => se puede agregar fintro adicionales. SQLAlchemiy devolvera otro objeto dentro de la clase

    preparaciones = orm.relationship(
        'PreparacionModel', backref='preparacionRecetas', lazy=True)
    
    recetas_ingredientes = orm.relationship(
        'RecetaIngredienteModel',backref='recetaIngredienteRecetas')


