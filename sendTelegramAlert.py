import requests
import os

def enviar_alerta_telegram(mensaje):
    token = os.getenv('TGM_TOKEN')  # Use environment variable for security
    chat_id = os.getenv('TGM_CHAT_ID')  # Use environment variable for security
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mensaje
    }
    requests.post(url, data=data)
