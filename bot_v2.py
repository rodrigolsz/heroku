import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Rutas correctas para Heroku
CHROMEDRIVER_PATH = "/app/.chrome-for-testing/chromedriver-linux64/chromedriver"
GOOGLE_CHROME_BIN = "/app/.chrome-for-testing/chrome-linux64/chrome"

# Configuración de Chrome
options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# Crear el servicio de ChromeDriver con la ruta correcta
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Lista de tokens a procesar
tokens = ["XDG9ER", "C5RZYQ"]

# IDs de los botones a hacer clic
button_ids = [
    "btnactiv_9bccbfb620d700c7",
    "btnactiv_c2182d10f040df31",
    "btnactiv_4879e7ffe83cf0dc",
    "btnactiv_8531d42b46ae25be"
]

def activar_dispositivo(driver, token):
    """Carga la página y activa los botones necesarios."""
    try:
        url = f"https://listasiptvactualizadas.com/activar-kraken-tv.php?token={token}"
        driver.get(url)
        print(f"Página cargada: {driver.title}")

        # Esperar 20 segundos para que los botones aparezcan
        time.sleep(20)

        # Intentar hacer clic en cada botón individualmente
        for btn_id in button_ids:
            try:
                boton = WebDriverWait(driver, 5).until(  # Espera hasta 5s por botón
                    EC.element_to_be_clickable((By.ID, btn_id))
                )
                boton_texto = boton.text.strip() if boton.text else "Botón sin texto"
                boton.click()
                time.sleep(2)  # Pequeña pausa entre clics
                print(f"Se activó el botón: {boton_texto}")
            except:
                print(f"No se encontró o no se pudo activar un botón con ID {btn_id}.")

        print(f"Dispositivos activados para token {token}.\n")

    except:
        print(f"Ocurrió un error durante la activación de {token}.")

# Ejecutar la activación para cada token
for token in tokens:
    activar_dispositivo(driver, token)

# Cerrar el navegador al final
driver.quit()
