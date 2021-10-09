import { DataTypes } from 'sequelize'
import { conexion } from '../config/sequelize'

//https://sequelize.org/master/manual/model-basics.html#column-options

export const tareaModel =()=>{
    return conexion.define(
        'tarea',
    {
        tareaId:{
            primaryKey:true,
            unique:true,
            autoIncrement:true,
            allowNull:false,
            field:'id',
            type:DataTypes.INTEGER
        },
        tareaNombre:{
            type:DataTypes.STRING(50),
            field:'nombre',
            allowNull:false
        },
        tareaHora:{
            type:DataTypes.TIME,
            field:"hora",
            allowNull:true,
        },
        tareaDias:{
            type:DataTypes.ARRAY(
                DataTypes.ENUM(["LUN","MAR","MIE","JUE","VIE","SAB","DOM"])
            ),
            field:"dias",
            allowNull:true,
        },
        
    },
    {
        tableName:"tareas",
        timestamps:true, //crear los campos de createdAt
        updatedAt:"fecha_de_actualizacion",
    });
}