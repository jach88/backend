import { MascotaSexo } from "./crear-mascota.dto";
import { IsOptional,IsString, IsEnum,IsDateString} from "class-validator";
import { BaseDto } from "../base.dto";

export class actualizarMascotaDto extends BaseDto{
    @IsString()
    @IsOptional()
    mascotaNombre:string;

    @IsString()
    @IsOptional()
    mascotaRaza:string;

    @IsEnum(MascotaSexo)
    @IsOptional()
    mascotaSexo:MascotaSexo;

    @IsDateString()
    @IsOptional()
    mascotaFechaNacimiento: Date;

}