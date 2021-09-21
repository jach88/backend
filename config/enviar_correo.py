from email.mime.text import MIMEText
import smtplib
#MIME= MultiPurpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
from os import environ
from dotenv import load_dotenv
load_dotenv()

mensaje = MIMEMultipart()
mensaje['From']= environ.get('EMAIL')
mensaje['Subject']='Solicitud de restauracion de contraseña'
password = environ.get('EMAIL_PASSWORD')

def enviarCorreo(destinatario, cuerpo):
    '''Funcion que sirve para enviar un correo'''
    mensaje['To'] = destinatario
    texto = mensaje
    #Luego de definir el cuerpo del correo agregamos al mesnaje mediante el metodo attach y em formato MIMEText en el cual recibira un texto y luego el format a convertir, si quieres convertri un html entonces podremos 'html', si queremos enviar un texto 'plain'
    mensaje.attach(MIMEText(cuerpo,'html'))
    try:
        #configurar el servidor smtp
        servidorSMPT = smtplib.SMTP('smtp.gmail.com',587)
        #indicar el protocolo de transferencia
        servidorSMPT.starttls()
        #inicio sesion en el servidor de correo con las credenciales asignadas previamente
        servidorSMPT.login(user=mensaje.get('from'), password=password)
        servidorSMPT.sendmail(
            from_addr=mensaje.get('From'),
            to_addrs=mensaje.get('To'),
            msg=mensaje.as_string()
        )
        #cerrar sesion del correo
        servidorSMPT.quit()
    except Exception as e:
        print(e)



