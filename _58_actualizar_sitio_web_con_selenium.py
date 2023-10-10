# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


"""ACTUALIZAR WEB CON SELENIUM

Podemos automatizar el refrescar sitios web con
selenium. Se requieren los siguientes paquetes:
pip install selenium
pip install webdriver-manager"""

url = 'https://www.google.com.mx/?hl=es'

# web driver from chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

while True:
    driver.refresh()
    time.sleep(5)
