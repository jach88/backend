import { IsDate, IsDateString, IsEnum, IsNotEmpty, IsString } from "class-validator";
import { BaseDto } from "../base.dto";


export enum MascotaSexo {
    MACHO="MACHO",
    HEMBRA="HEMBRA",
}

export class crearMascotaDTO extends BaseDto {
    @IsString()
    @IsNotEmpty()
    mascotaNombre:string;

    @IsString()
    @IsNotEmpty()
    mascotaRaza:string;

    @IsEnum(MascotaSexo)
    @IsNotEmpty()
    mascotaSexo:MascotaSexo;

    @IsDateString()
    @IsNotEmpty()
    mascotaFechaNacimiento: Date;

    @IsString()
    @IsNotEmpty()
    clienteId:string
}