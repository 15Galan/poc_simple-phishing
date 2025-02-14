#!/usr/bin/env python3


import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Cargar variables desde el archivo .env
load_dotenv()

# Configuración del servidor SMTP desde el .env
smtp_servidor = os.getenv('SMTP_SERVER')
smtp_puerto = int(os.getenv('SMTP_PORT'))  # Convertir a entero
smtp_usuario = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASS')

# Configuración del remitente y destinatario
destinatario = os.getenv('TARGET')
remitente = destinatario

# Crear el mensaje de correo falso
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = '¡Enhorabuena!'

cuerpo = '<b>Ha ganado usted un sorteo.</b> Visite <a href="http://srgalan.com">srgalan.com</a> para reclamar su premio.'
mensaje.attach(MIMEText(cuerpo, "html"))

print('Cuerpo del correo creado.')

# Enviar el correo
try:
    # Iniciar el servidor SMTP
    servidor = smtplib.SMTP(smtp_servidor, smtp_puerto)
    servidor.starttls()

    print(f'Conexión con "{smtp_servidor}" creada.')
    print(f'Enviando correo para "{destinatario}"...')

    # Enviar el correo usando
    servidor.login(smtp_usuario, smtp_password)
    servidor.sendmail(remitente, destinatario, mensaje.as_string())

    print('\n\033[92mCorreo enviado.\033[0m')

    # Apagar el servidor
    servidor.quit()

except Exception as e:
    print(f'\n\033[91mCorreo NO enviado: {str(e)}\033[0m')
