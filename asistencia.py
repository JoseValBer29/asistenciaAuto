# asistencia.py - Script para automatizar el marcado de asistencia en una plataforma web

from selenium import webdriver  # Selenium para automatización de navegador
from selenium.webdriver.common.by import By  # Para seleccionar elementos en la página
import time  # Para pausas temporales
import os  # Para acceder a variables de entorno

import sendMail as mail  # Módulo propio para enviar correos
import sendTelegramAlert as tel  # Módulo propio para alertas por Telegram


def marcar_asistencia():
    print("Iniciando el proceso de marcar asistencia...")  # Mensaje informativo en consola

    # Obtiene credenciales y URL desde variables de entorno por seguridad
    usuario = os.getenv('USER_AUTOMATION')  # Usuario de la plataforma
    clave = os.getenv('PASSWORD_AUTOMATION')  # Contraseña de la plataforma
    url = os.getenv('URL_AUTOMATION')  # URL de la plataforma

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Ejecuta el navegador en modo headless (sin interfaz gráfica)

    driver = webdriver.Firefox(options=options)  # Inicializa el navegador Firefox
    
    try:
        # Accede a la página de inicio de sesión
        driver.get(url)

        # Ingresa usuario y contraseña en el formulario
        driver.find_element(By.NAME, "usuario").send_keys(usuario)
        driver.find_element(By.NAME, "clave").send_keys(clave)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)  # Espera a que cargue la página siguiente

        # Busca y hace clic en el botón de marcar asistencia
        boton_asistencia = driver.find_element(By.PARTIAL_LINK_TEXT,"TURNO")
        print(boton_asistencia.text)  # Muestra el texto del botón en consola
        boton_asistencia.click()

        # Confirma la acción en el cuadro de diálogo
        driver.find_element(By.CSS_SELECTOR, "button[class='ajs-button ajs-ok']").click()

        driver.quit()  # Cierra el navegador

        # Envía correo y alerta de éxito
        mail.enviarCorreo()
        tel.enviar_alerta_telegram('''✅ Asistencia marcada con éxito.
                                    ¡Despierta y disfruta del día!''')
    except Exception as e:
        # Si ocurre un error, muestra el error, cierra el navegador y envía alerta de fallo
        print(f"Error al marcar asistencia: {e}")
        driver.quit()
        tel.enviar_alerta_telegram('''🚨 Fallo al marcar la asistencia.
                                    ¡Despierta y márcala tú mismo!''')