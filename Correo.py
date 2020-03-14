import re
import smtplib

correo = input ("Escriba su correo :")
verificado = re.search('\w+@\w+.\w+', correo)
if verificado == None:
    print("su correo no es valido")
    exit()# si no es correo valido se sale del programa



gmail_user = 'danielhmorenog@gmail.com'
gmail_password = 'knjaonvxvxjqaewn'

sender = 'danielhmorenog@gmail.com'
receivers = [correo]
asunto = input ("Escriba el asunto del correo a enviar :")
cuerpo = input ("Escriba el mensaje a enviar:")
mensaje = """ From: Daniel Moreno <danielhmorenog@gmail.com>
To: """ +correo +"""
Subject: """+asunto+""" 

"""+cuerpo
try:
  smtpObj = smtplib.SMTP('smtp.gmail.com',587)
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login(gmail_user, gmail_password)
   
  smtpObj.sendmail(sender, receivers, mensaje)
  smtpObj.quit()  
  print ("correo enviado correctamente")
except smtplib.SMTPException:
  print ("Error: no se pudo enviar el correo")
