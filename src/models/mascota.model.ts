import { Schema } from "mongoose";

const mascotaSchema = new Schema({
    mascotaNombre:{
        type:Schema.Types.String,
        alias:"nombre"
    },
    mascotaRaza:{
        type:Schema.Types.String,
        alias:"raza"
    },
    mascotaSexo:{
        type:Schema.Types.String,
        enum:["MACHO","HEMBRA"],
        alias:"sexo"
    },
    mascotaFechaNacimiento:{
        type: Schema.Types.Date,
        alias:"fecha_nac"
    }
})