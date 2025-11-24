# SQA_scripts_automatizables
Práctica de pruebas automáticas utilizando Python + Selenium WebDriver para validar funcionalidades del sitio de práctica https://www.saucedemo.com

Estructura del Repositorio
SeleniumScripts/
│
├── scripts/
│   ├── script_prueba_de_agregar_al_carrito.py
│   ├── script_prueba_de_compra_completa_de_productos.py
│   └── script_prueba_eliminacion_de_producto_del_carrito
│
└── exechrome/
      chromedriver.exe
      
Incluye el archivo chromedriver.exe, necesario para que Selenium pueda controlar el navegador Chrome.
En este caso use la version mas reciente de chrome 142.0.7444.176 y la de chromedriver es 142.0.7444.175

1. Requisitos previos
Python 3.10 o superior
Navegador Google Chrome instalado (ver. 142.0.7444.176)
ChromeDriver incluido en exechrome/ (para que funcione recomiendo descargar toda la carpeta de SeleniumScripts y ejecutar
desde la respectiva carpeta los scripts, en caso de que no funcione probablemente no es la misma version de Chrome a la que nosotros utilizamos)

Ejecución de los Scripts
2. Instalar dependencias (Selenium)
pip install selenium 
instalar python (3.13.5 en nuestro caso)


3. Ejecutar cualquier script
Ejemplo:
python scripts/script_prueba_de_agregar_al_carrito.py


