from sqlalchemy.sql.schema import ForeignKey
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class PreparacionModel(base_de_datos.Model):
    __tablename__= "preparaciones"

    preparacionId = Column(type_=types.Integer, name='id',
                           primary_key=True, autoincrement=True, unique=True)

    preparacionOrden = Column(type_=types.Integer, name='orden', default=1)

    preparacionDescripcion = Column(type_=types.Text, name='descripcion', nullable=False)


    # asi se crean las realaciones
    # en el parametro column => el nombre de la tabla y su columna
    # ondelete=> idncar que accion debe de tomar el hijo (tabla donde esta ubicada de FK) cuando se elimine el registro de la fk
    # CASCADE => eliminar el registro de recetas y luego todos los registros ligados a esa receta
    # DELETE => se eliminara y dejara a las FK con el mismo valor aunque este ya no exista
    # RESTRINCT => restringe y prohibe la eliminacion de las recetras que tengan preparaciones (primero tednemos que eliminar las preparaciones y luego recien a la receta)
    #none => eliminalo y en las preparaciones seta el valor de la receta a null
    #https://docs.sqlalchemy.org/en/14/core/constraints.html?highlight=ondelete#sqlalchemy.schema.ForeignKey.params.ondelete
    receta = Column(ForeignKey(column='recetas.id', ondelete='RESTRICT'),
                    name='recetas_id', type_=types.Integer, nullable=False)
    
    def __str__(self):
        return self.preparacionDescripcion