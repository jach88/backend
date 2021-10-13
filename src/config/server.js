import express,{ json } from 'express';
import { tareasRouter } from '../routes/tareas.routes';
import { conexion } from './sequelize';
import swagger from "swagger-ui-express"
import documentacion from "../../swagger_tareas.json";
import cors from "cors";

export class Server{
    constructor(){
        this.app = express();
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
        this.puerto = process.env.PORT || 8000;
        this.app.use(cors({
            origin: "*" ,   //['https://mipagina.com','https://cms.mipagina.com']
            methods:"PUT", //EN EL CASO QUE LOS METODOS SIEMPRE EL GET SERA PERMITIDO SIEMPRE
            allowedHeaders:["Content-type"],
        }));
        this.bodyParser();
        this.rutas();
    
    }
    bodyParser(){
        this.app.use(json());
    }
    rutas(){
        
        this.app.get("/",(req,res) => {
            res.json({
                message: "Bienvenidos a mi API",
            });
        });

        // process.env.NODE_ENV === "production"
        // ? ((documentacion.host = "https://tareas-express-eduardo.herokuapp.com/"),
        //   (documentacion.schemes = ["https"]))
        // : ((documentacion.host = `http://127.0.0.1;${this.puerto}`),
        //   (documentacion.schemes = ["http"]));

        if (process.env.NODE_ENV === "production") {
            documentacion.host = "tareas-express-christian.herokuapp.com/";
            documentacion.schemes = ["https"];
      } else {
            documentacion.host = `127.0.0.1;${this.puerto}`;
            documentacion.schemes = ["http"];
      }


        this.app.use('/docs',swagger.serve, swagger.setup(documentacion));

        this.app.use(tareasRouter);
    }
    start(){
        this.app.listen(this.puerto,async ()=>{
            console.log(
                `Servidor corriendo exitosamente en el puerto ${this.puerto}`
            );
                try {
                   await conexion.sync()
                   console.log("Base de datos conectada exitosamente")
                } catch (error) {
                    console.log(error)
                }
            
        });
    }
}