import { DataTypes } from 'sequelize'
import conexion from '../config/sequelize'

export default () =>conexion.define(
    'compras',{
        compraId:{
            type:DataTypes.UUID,
            defaultValue:DataTypes.UUIDV4,
            field:'id',
            primaryKey:true,   
        },

        compraFecha:{
            type:DataTypes.DATE,
            field:'total',
            validate:{
                min:0,
            },
            allowNull:false,
        },
        
    },
    {
        tableName:"compras",
        timestamps:false,
    }    
);

