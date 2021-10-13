import {Sequelize} from 'sequelize'
require("dotenv").config();

export const conexion = new Sequelize(
    process.env.DATABASE_URL,
    {
        logging:false,
    //para poder utilizar bd remotas de postgres que requieran configuracion especial
        dialectOptions:
            process.env.NODE_ENV === "production" //variable que define heroku en sus servidores indicando el contenido de production
                ?{
                    //sirve para indicar que la bd no sea necesaria que tenga certificado SSL
                    ssl:{
                        rejectUnauthorized:false,
                    },
                }
                :{},
    }
    );

