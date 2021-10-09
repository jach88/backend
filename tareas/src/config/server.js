import express,{ json } from 'express';
import { tareasRouter } from '../routes/tareas.routes';
import { conexion } from './sequelize';

export class Server{
    constructor(){
        this.app = express();
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
        this.puerto = process.env.PORT || 8000;
        this.bodyParser();
        this.rutas();
    
    }
    bodyParser(){
        this.app.use(json());
    }
    rutas(){
        this.app.use(tareasRouter)
        this.app.get("/",(req,res) => {
            res.json({
                message: "Bienvenidos a mi API",
            });
        });
    }
    start(){
        this.app.listen(this.puerto,async ()=>{
            console.log(
                `Servidor corriendo exitosamente en el puerto ${this.puerto}`
            );
                try {
                   await conexion.sync()
                } catch (error) {
                    console.log(error)
                }
            
        });
    }
}