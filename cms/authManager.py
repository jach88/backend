from django.contrib.auth.models import BaseUserManager
#el baseusermanager sirve para modificar el comportamiento de un usuario por consola, nos permite modificar por completo al modelo auth
#usermanager nos permite modificar campos como el firsname y lastname agregar nuevos campos


class ManejoUsuarios(BaseUserManager):
    
    def create_user(self, email, nombre, apellido, tipo, password= None):
        """Creacion de un usuario"""
        if not email:
            raise ValueError('El usuario tiene que tener un correo valido')
        #validar mi correo y ademas lo normalizo haciendolo todo en minusculas
        email = self.normalize_email(email)
        #creo mi instancia de usuario
        usuarioCreado = self.model(usuarioCorreo= email, usuarioNombre= nombre, 
                                   usuarioApellido=apellido, usuarioTipo=tipo)

        #set_password() => encriptara la contraseña
        usuarioCreado.set_password(password)
        #sirve para referemcia a que base de datos estoy haciendo la creacion, esto se utilizara mas que todo para cuando tengamos multiples bases de datos en nuestro proyecto
        usuarioCreado.save(using=self._db)

        return usuarioCreado
    
    def create_superuser(self, usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password):
        '''Creacion de un super usuario (administrador)'''
        #los parametros tienen que ser los mismos que hubiesemos declarado en el usuarioModel REQUIRED_FIELD y en el username_field llegaran con esos mismo nombre

        nuevoUsuario = self.create_user(
            usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password)
        
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)




