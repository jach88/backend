from django.contrib import admin
from .models import ClienteModel, ProductoModel

class ProductiAdmin(admin.ModelAdmin):
    #modificar la vista del modelo
    #no funciona el signo menos para que muestre descendente
    list_display = ['productoId','productoNombre', 'productoPrecio']
    #agregar un buscador para hacer busquedas
    search_fields = ['productoNombre','productoUnidadMedida']
    #crea un campo de busqueda de acceso rapido
    list_filter = ['productoUnidadMedida']
    #indico si se desea ver algun campo que el usuario no puede manipular
    readonly_fields = ['productoId']

admin.site.register(ClienteModel)
#si nosotros queremos modificar la visualizaciion y comportamiento de nuestro panel administrativo para un determinado modelo
admin.site.register(ProductoModel, ProductiAdmin)