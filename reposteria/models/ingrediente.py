from os import name
from conexion_bd import base_de_datos
from sqlalchemy import Column, types



class IngredienteModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    
    ingredienteId = Column(name='id', type_=types.Integer, primary_key=True,
                            unique=True, autoincrement=True, nullable=False)
    
    ingredienteNombre = Column(name='nombre', type_=types.String(
        length=45),nullable=False, unique=True)

    def __str__(self):
        print(self.ingredienteId)
        # return 'El ingrediente es: %s' % self.ingredienteNombre
        return 'El ingrediente es:{}'.format(self.ingredienteNombre)
