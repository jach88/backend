from rest_framework import serializers
from .models import ProductoModel

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        #esto vinculara el serializador con el modelo respectivo para jalar los atributos y hacer las validaciones correspondientes
        model = ProductoModel

        #indica que campos tengo que mostrar para la deserealizacion
        #fields ='__all__' => indicará que haremos uso de todas los atributos del retorno de elementos los atributos del modelo
        fields = '__all__'
        #fields=['productoNombre','ProductoPrecio']
        
        #exclude =['campo1','campo2'] => excluira tanto de la peticion como el retorno de elementos los atributos indicados
        # exclude = ['productoId']

        #no se puede utilizar los dos atributos al mismo tiempo, es decir, o usamos el exclude o usamos el fields