# Import smtplib for the actual sending function
import smtplib
import datetime
import sendTelegramAlert as tel
import os

username = os.getenv('GMAIL_USER')  
password = os.getenv('GMAIL_PASSWORD')  

destination = os.getenv('GMAIL_DESTINATION')  # Use environment variable for security

# Import the email modules we'll need
from email.message import EmailMessage

tiempo = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(tiempo)
mensaje = "Esto es una prueba" + tiempo
msg = EmailMessage()
msg.set_content(mensaje)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'ESTO ES UNA PRUEBA'
msg['From'] = username
msg['To'] = destination

# Send the message via our own SMTP server.
smtp_server = 'smtp.gmail.com'
smtp_port = 587

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Encriptar conexión
        server.login(username, password)
        server.send_message(msg)
        print("Correo enviado con éxito.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
    tel.enviar_alerta_telegram("🚨 Fallo en el envío del correo de prueba. ¡Despierta y envíalo tú mismo!")
