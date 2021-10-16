import { plainToClass } from 'class-transformer';
import { validate } from 'class-validator';
import {Request, Response} from 'express'
import { Usuarios } from '../config/models';
import { RegistroDto } from '../dtos/request/registro.dto';
import { UsuarioDto } from '../dtos/response/usuario.dto';
import { sign, SignOptions } from "jsonwebtoken";
import usuariosModel, { TipoUsuario } from '../models/usuarios.model';
import { LoginDto } from '../dtos/request/login.dto';
import { compareSync } from 'bcrypt';
import { RequestUser } from "../middlewares/validator"
import { v2 } from "cloudinary"

interface Payload {
    usuarioNombre: string
    usuarioId: string
    usuarioFoto?: string
    usuarioTipo: TipoUsuario
  }

const tokenOptions:SignOptions ={
    expiresIn:'1h'
}

export const registroController = async(req: Request, res:Response) =>{
    try {
        const { body } = req;

        const data = plainToClass(RegistroDto,body);
        const validacion = await validate(data);
        console.log(validacion);
        if (validacion.length !== 0 ){
            const mensajes = validacion.map((error) => error.constraints);

            return res.status(400).json({
                content:validacion,
                message:"Error en los valores"
            });
        }

        const usuarioEncontrado = await Usuarios.findOne({
            where: {usuarioCorreo:body.usuarioCorreo },
        });

        if(usuarioEncontrado){
            return res.status(400).json({
                content:null,
                message:"Usuario ya existe"
            });
        }

        const nuevoUsario = await Usuarios.create(body);

        const content = plainToClass(UsuarioDto,nuevoUsario.toJSON());

        const payload: Payload = {
            usuarioId: nuevoUsario.getDataValue("usuarioId"),
            usuarioNombre: nuevoUsario.getDataValue("usuarioNombre"),
            usuarioTipo:nuevoUsario.getDataValue("usuarioTipo"),
            usuarioFoto:nuevoUsario.getDataValue("usuarioFoto"),
        };

        sign(payload,process.env.JWT_TOKEN?? "",{expiresIn:"1h"})
        //metodo alternativo
        //primero se construye el objeto
        //const nuevoUsario2 = Usuarios.build({usuarioNombre:'Christian'})
        //nuevoUsario2.setDataValue('usuarioNombre','asasas')
        //se guarda en la bd
        //await nuevoUsario2.save()
        

        return res.status(201).json({
            content,
            message:"Usuario creado exitosamente"
        });
    } catch (error) {
        if(error instanceof Error){

            return res.status(400).json({
                message:"Error al crear el usuario",
                content:error.message,
            });
        }
    }
};

export const login = async (req: Request, res: Response)=>{
    //dto
    const validador = plainToClass(LoginDto,req.body)
    try {
        const resultado = await validate(validador);

        if(resultado.length !== 0){
            return res.status(400).json({
                content: resultado.map((error)=>error.constraints),
                message:"Informacion incorrecta",
            });
        }

        const usuarioEncontrado = await Usuarios.findOne({
            where:{usuarioCorreo: validador.correo },
        });

        if(!usuarioEncontrado){
            return res.status(400).json({
                message:"Usuario Incorrecto",
                content:null,
            });
        }

        const resultado_password = compareSync(
            validador.password,
            usuarioEncontrado.getDataValue("usuarioPassword")
        );

        if(!resultado_password){
            return res.status(400).json({
                message:"Usuario incorrecto",
                content:null,
            });
        }

        const payload: Payload = {
            usuarioId: usuarioEncontrado.getDataValue("usuarioId"),
            usuarioNombre: usuarioEncontrado.getDataValue("usuarioNombre"),
            usuarioTipo:usuarioEncontrado.getDataValue("usuarioTipo"),
            usuarioFoto:usuarioEncontrado.getDataValue("usuarioFoto"),
        };

        const jwt = sign(payload, process.env.JWT_TOKEN ?? "", tokenOptions);

        return res.json({
            content: jwt,
            message: null,
        });

    }catch(error){
        // console.log(error);
        if(error instanceof Error){

            return res.status(400).json({
                message:"error al hacer el login",
                content: error.message,
            });
        }
    }
};

export const perfil = (req:RequestUser, res:Response)=>{
    const content = plainToClass(UsuarioDto,req.usuario);
    if (!content.usuarioFoto){

        console.log(content.usuarioNombre);
        let [nombre, apellido] = content.usuarioNombre.split(" ");

        content.usuarioFoto =`https://avatars.dicebear.com/api/initials/${
            nombre[0]
        }${apellido ? apellido[0] : ""}.svg`;
    } else{
        const url =v2.url(content.usuarioFoto);
        content.usuarioFoto=url;
    }
    return res.json({
        message:"Hola desde el endpoint final",
        content,
    });
};



export const actualizarPerfil = (req:RequestUser, res: Response)=>{
    //Tarea
    //hacer un patch para que el usuario pueda modificar su nombre, su correo, su foto o su contraseña
    // req.usuario = ya tiene toda la info del usuario
    // usuario Foto usuario/asdasdasds
    // forma de eliminar imagenes de cloudinary
    // await v2.
}