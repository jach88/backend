import express, {json, raw} from "express";
import morgan from "morgan";
import { actividades_router } from "../routes/actividades";


export class Server{
    constructor(){
        this.app = express();
        this.puerto = 8000;
        this.cors();
        this.bodyParser();
        this.rutas();        
    }
    
    bodyParser(){
        //Sirve oara indicar en el proyecto que formatos (bodys) me puede enviar el front (client)
        this.app.use(json());
        this.app.use(raw())
    }

    rutas(){
        //agregamos el middleware de morgan para que haga tracking a las consultas al backend
        this.app.use(morgan('dev'));
        this.app.use(actividades_router);

        this.app.get('/',(req,res) => {
            //req => Request  => la informacion que me enviara el cliente
            //res => Response => la informacion que le voy a dar  
            res.send("Bienvenido a mi API");
    });
    }

    cors(){
        this.app.use((req, res,next)=>{
            //Access-Control-Allow-Origin => indica que origenes pueden acceder a mi api (si queremos todos ponemos el *)
            res.header("Access-Control-Allow-Origin","*")
            //Access-Control-Allow-Headers => INDICA LAS CABECERAS PERMITIDAS QUE PUEDE ENVIAR EL CLIENTE
            res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
            //Access-Control-Allow-Methods => iNDICA LOS METODOS A LOS QUE PUEDE ACCEDER MI CLIENTE
            res.header("Access-Control-Allow-Methods","GET, POST, PUT, DELETE")
            next()
        })
    }



    start(){
        this.app.listen(this.puerto, ()=>{
            console.log(`Servidor corriendo en el puerto ${this.puerto}`)
        })
    }
}