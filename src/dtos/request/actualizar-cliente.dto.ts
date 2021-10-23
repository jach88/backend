import { IsEmail, IsNotEmpty, IsOptional, IsString, MaxLength, MinLength } from "class-validator";
import { BaseDto } from "../base.dto";

export class ActualizarClienteDto extends BaseDto{
    @IsString()
    @IsNotEmpty()
    @IsOptional()
    clienteNombre: string;

    @IsOptional()
    @IsNotEmpty()
    @IsString()
    clienteApellido: string;

    @IsOptional()
    @IsNotEmpty()
    @IsEmail()
    clienteCorreo: string;

    @IsOptional()
    @IsNotEmpty()
    @MinLength(7)
    @MaxLength(9)
    clienteDni?: string;
}