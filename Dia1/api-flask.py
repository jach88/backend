from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos = [{
    "nombre":"Palta fuerte",
    "precio": 5.20
},{
    "nombre":"Albahaca 100gr",
    "precio": 0.80
}]

@app.route("/")
def inicio():
    # siempre que vamos a responder al cliente tiene que ser por el return
    return {
        "message":"Bienvenidos a mi API",
        "content":""
    }

@app.route("/productos", methods=['POST','GET'])
def gestion_productos():

    print(request.method)
    if request.method == 'GET':
        return{
            "message": "",
            "content": productos
        }

    elif request.method == 'POST':
    #el get_json() sirve para visualizar toda la informacion que el usuario me esta enviando por el body
    #el body es el cuerpo de la peticion (donde el front adjunta la informacion que quiere enviar)
    #el body se envia en formato JSON | multipart | TEXT | XML
        producto = request.get_json()
        productos.append(producto)
        return{
            "message": "Producto Creado exitosamente",
            "content": producto
        }, 201

@app.route("/producto/<int:id>", methods=['GET','PUT', 'DELETE'])
def gestion_producto(id):

    
    #buscar la posicion en la lista
    #si no existe indicar que no existe
    #si existe, mostrar el producto
        total_productos = len(productos)    #primero sacamos la longitud
        if id<total_productos:
            if request.method =="GET":
                return{
                    "content": productos[id],
                    "message": None
                }, 200
            elif request.method == "PUT":
                data = request.get_json()
                productos[id] = data
            
                return {
                    "content":productos[id],
                    "message": "Producto actualizado exitosamente"
                },201
                
            elif request.method =="DELETE":
                del productos[id]

                return{
                    "content":None,
                    "message":"Producto eliminado exitosamente"
                }
        else:
            return{
                "message": "Producto no encontrado",
                "content": None
            },404



if __name__ == "__main__":
    app.run(debug=True)