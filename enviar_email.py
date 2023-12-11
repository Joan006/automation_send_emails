"""
codigo : Este codigo sera para la automatizacion para enviar emails con gmail.
@utor : joan martinez , 'andv' 
"""
import os
# importamos el modulo de email.message para trabajar con mensajes de correo electronico
from email.message import EmailMessage
# seguridad estándar que garantiza que la conexión entre un cliente y un servidor
import ssl
import smtplib
import imghdr

# Se crean las variables que representan el cuerpo del correo
email_emisor = 'martinez.olivares.006@gmail.com'
email_contraseña = 'ixcf nqak pxak ueir'
email_receptor = 'joan_martinez.olivares@hotmail.com'
asunto = 'Prueba autmatizacion'
cuerpo = 'Esto es una prueba de la automatizacion creada'


em = EmailMessage()
# establecer los campos principales (Subject, From, To)
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)
# .set_content , se utiliza para establecer el cuerpo del email

# Adjuntar archivo 
with open('loki.jpeg', 'rb') as file:
  file_data = file.read()
  file_tipo = imghdr.what(file.name)
  file_nombre = file.name
em.add_attachment(file_data, filname=file_nombre, subtype=file_tipo, maintype='image')


contexto = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
  smtp.login(email_emisor, email_contraseña)
  smtp.sendmail(email_emisor, email_receptor, em.as_string())

