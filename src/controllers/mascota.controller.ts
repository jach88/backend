import { rejects } from "assert";
import { plainToClass } from "class-transformer"
import { Request,Response } from "express";
import { HttpError } from "http-errors";
import { actualizarMascotaDto } from "../dtos/request/actualizar-mascota.dto";
import { crearMascotaDTO } from "../dtos/request/crear-mascota.dto"
import Cliente from "../models/cliente.model";

export const crearMascota = async (req:Request, res:Response) =>{
    const dto = plainToClass(crearMascotaDTO,req.body);
    try {
        await dto.isValid();

        const{clienteId, ...mascota } = dto;
        //buscar cliente por id
        const clienteEncontrado = await Cliente.findById(clienteId);

        if(!clienteEncontrado){
            return res.json({
                    message:"Cliente no existe",
                    content:null,
                });
        }

        console.log(clienteEncontrado);
        clienteEncontrado.clienteMascotas.push(mascota);

        const resultado = await clienteEncontrado.save();

        return res.status(201).json({
            message:"Mascota registrada exitosamente",
            content:resultado,
        })        //si no existe indicar un message que no existe
        //message:"Cliente no existe" status 200

    } catch (error) {
        if (error instanceof HttpError){
            return res.status(error.status).json(error)
        }
    }
};

export const actualizarMascota = async (req:Request, res:Response)=>{
    const dto = plainToClass(actualizarMascotaDto,req.body);
    const{mascotaId, clienteId }=req.params;
    try {
        await dto.isValid()
        
        //encontrar ese cliente
        const clienteEncontrado = await Cliente.findById(clienteId)
        if(!clienteEncontrado){
                return res.json({
                    message:"Cliente no encontrado"
                })
            }
        //iterar el array de mascotas para encontrar esa mascota
        const { clienteMascotas } = clienteEncontrado;

        for(const mascota of clienteMascotas){
            console.log(mascota._id);

            if(mascota._id && mascota._id == mascotaId){
                console.log("si hay la mascota");
                mascota.mascotaFechaNacimiento = dto.mascotaFechaNacimiento ?? mascota.mascotaFechaNacimiento;
                mascota.mascotaNombre = dto.mascotaNombre ?? mascota.mascotaNombre;
                mascota.mascotaRaza = dto.mascotaRaza ?? mascota.mascotaRaza;
                mascota.mascotaSexo = dto.mascotaSexo ?? mascota.mascotaSexo;

                await clienteEncontrado.save();
                return res.json({
                    message:"Mascota actualizada exitosamente",
                    content: mascota
                });
            }
        }
        
        //actualizar esa mascota

        //si en algun momento(cliente no existe, mascota mo existe) emitir una respuesta que indique que no encontro dicha entidad
        return res.json({
            message:"Mascota actualizada exitosamente"
        })
    } catch (error) {
        if(error instanceof HttpError){
            return res.status(error.status).json(error);
        }
    }
}
