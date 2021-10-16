import comprasModel from "../models/compras.model";
import detallesModel from "../models/detalles.model";
import productosModel from "../models/productos.model";
import usuariosModel from "../models/usuarios.model";

//RELACIONES
export const Compras = comprasModel();
export const Detalles = detallesModel();
export const Productos = productosModel();
export const Usuarios = usuariosModel();

// Productos.sync({force:true})

//Productos tiene muchos detalles
Productos.hasMany(Detalles,{
    foreignKey: {name:"productoId", allowNull: false, field:"producto_id"},
});
//Detalle pertenece a un Producto
Detalles.belongsTo(Productos,{
    foreignKey:{ name:"productoId", allowNull:false, field:"producto_id"},
});

Compras.hasMany(Detalles,{
    foreignKey:{ name:"compraId",allowNull:false,field:"compra_id"}
});
Detalles.belongsTo(Compras,{
    foreignKey:{ name:"productoId", allowNull:false, field:"compra_id"},
});
Compras.belongsTo(Usuarios,{
    foreignKey:{ name:"productoId", allowNull:false, field:"usuario_id"},
});
Usuarios.hasMany(Compras,{
    foreignKey:{ name:"usuarioId",allowNull:false, field:"usuario_id"}
})


