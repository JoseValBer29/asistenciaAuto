# sendMail.py - Script para enviar un correo de notificación de asistencia y alertar por Telegram si falla

# Import smtplib for the actual sending function
import smtplib  # Librería estándar para enviar correos electrónicos
import datetime  # Para trabajar con fechas y horas
from datetime import timezone, timedelta  # Para manejo de zona horaria
import sendTelegramAlert as tel  # Módulo propio para alertas por Telegram
import os  # Para acceder a variables de entorno
from email.message import EmailMessage  # Para construir el mensaje de correo


def enviarCorreo():
    print("Iniciando el envío del correo...")  # Mensaje informativo en consola

    # Obtiene las credenciales y destinatario desde variables de entorno por seguridad
    username = os.getenv('GMAIL_USER')  # Correo del remitente
    password = os.getenv('GMAIL_PASSWORD')  # Contraseña del remitente
    destination = os.getenv('GMAIL_DESTINATION')  # Correo del destinatario

    # Define la zona horaria (UTC-5)
    tzone = timezone(timedelta(hours=-5))

    # Obtiene la hora actual en la zona horaria definida y la formatea
    tiempo = str(datetime.datetime.now(tzone).strftime("%Y-%m-%d %H:%M:%S"))
    print(tiempo)  # Muestra la hora de envío en consola
    mensaje = "Se marcó la asistencia a las " + tiempo  # Mensaje del correo

    # Construye el mensaje de correo
    msg = EmailMessage()
    msg.set_content(mensaje)
    msg['Subject'] = f'Asistencia Marcada'  # Asunto del correo
    msg['From'] = username  # Remitente
    msg['To'] = destination  # Destinatario

    # Configuración del servidor SMTP de Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        # Conexión y envío del correo
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Inicia conexión segura (TLS)
            server.login(username, password)  # Autenticación
            server.send_message(msg)  # Envía el mensaje
            print("Correo enviado con éxito.")
    except Exception as e:
        # Si falla, muestra el error y envía alerta por Telegram
        print(f"Error al enviar el correo: {e}")
        tel.enviar_alerta_telegram('''🚨 Fallo en el envío del correo de prueba.
                                   ¡Despierta y revisa si se marcó la asistencia!''')
        
if __name__ == "__main__":
    enviarCorreo()  # Ejecuta el envío de correo al correr el script directamente
    tel.enviar_alerta_telegram('''✅ Correo de prueba enviado con éxito.
                                ¡Despierta y disfruta del día!''')  # Alerta de éxito por Telegram
