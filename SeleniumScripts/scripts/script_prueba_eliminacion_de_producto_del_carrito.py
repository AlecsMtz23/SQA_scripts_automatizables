import os #Para despues obtener el directorio donde esta el chromedrive
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Directorio donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al chromedriver en ../exechrome/
# Esta hecho asi para que funcione en cualquier PC
# Siempre y cuando descargues toda la carpeta desde el GitHub
driver_path = os.path.join(BASE_DIR, "..", "exechrome", "chromedriver.exe")

service = Service(driver_path)

options = Options()
options.add_argument("--guest")  # Modo invitado para evitar el popup de contraseñas, de lo contrario falla el script

driver = webdriver.Chrome(service=service, options=options)

# ====================================
#   CASO DE PRUEBA CP-05
# ====================================

# Abrir página
driver.get("https://www.saucedemo.com/")
time.sleep(1)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Agregar producto
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# Ir al carrito
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Eliminar producto
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(1)

# Validar que ya no hay productos
items = driver.find_elements(By.CLASS_NAME, "cart_item")

if len(items) == 0:
    print("Caso de prueba aprobado: Producto eliminado correctamente.")
else:
    print("Error: Todavía hay productos en el carrito.")

time.sleep(3)
driver.quit()
