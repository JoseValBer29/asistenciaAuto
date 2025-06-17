import asistencia  # Módulo propio para marcar asistencia
import datetime  # Para trabajar con fechas y horas
import time  # Para pausas temporales
import numpy as np  # Para generación de números aleatorios

if __name__ == "__main__":
    # Punto de entrada principal del script

    print("Iniciando el proceso...")
    print(f"Fecha y hora actual UTC: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Comprobando si es un día laborable...")

    # Lista de días feriados (formato: 'dd-mm')
    dias_feriados = ['29-06','23-07','28-07','29-07','06-08',
                     '30-08','08-10','01-11','08-12','09-12',
                     '25-12','01-01','01-05','07-06']
    dia_actual = datetime.datetime.now().strftime("%d-%m")  # Día actual en formato 'dd-mm'

    # Si hoy no es feriado, proceder con el marcado de asistencia
    if dia_actual not in dias_feriados:
        np.random.seed(0)  # Fijar semilla para reproducibilidad
        minuto = np.random.randint(0, 300)  # Genera un tiempo aleatorio entre 0 y 299 segundos
        print(f"Tiempo de espera aleatorio: {minuto//60} minutos y {minuto%60} segundos")
        
        # Esperar un tiempo aleatorio antes de marcar asistencia
        time.sleep(minuto)
        print("Iniciando el script de asistencia...")
        try:
            asistencia.marcar_asistencia()  # Llama a la función principal de asistencia
        except Exception as e:
            print(f"Error al marcar asistencia: {e}")
    else:
        print("Hoy es un día feriado, no se marcará asistencia.")

