import requests  # Librería para hacer peticiones HTTP
import os  # Para acceder a variables de entorno


def enviar_alerta_telegram(mensaje):
    # Obtiene el token y chat_id de Telegram desde variables de entorno por seguridad
    token = os.getenv('TGM_TOKEN')  # Token del bot de Telegram
    chat_id = os.getenv('TGM_CHAT_ID')  # ID del chat de Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"  # URL de la API de Telegram
    data = {
        "chat_id": chat_id,  # Destinatario del mensaje
        "text": mensaje      # Contenido del mensaje
    }
    requests.post(url, data=data)  # Envía la alerta por Telegram
