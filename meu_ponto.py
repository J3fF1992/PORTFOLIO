import time
import selenium
from selenium import webdriver
import pyautogui
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r'msedgedriver.exe'
driver = webdriver.Edge(executable_path=driver_path)
driver.get('https://login.lg.com.br/login/leafpay_provu')
driver.maximize_window()
time.sleep(5) 
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form0"]/div[4]')))   
pyautogui.typewrite('jefferson.reis@provu.com.br')  # Digitar credencias
time.sleep(5)  # Aguarda um pouco para a página carregar completamente
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite('Xtz081992@')
pyautogui.press('enter')
time.sleep(8)
wait = WebDriverWait(driver, 10) #guarda o botão aparecer
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/section/section/div[1]/div[5]/div/div/div/div[2]/div/div/div/div/div[1]/button/span[1]')))  #localizar o botão de click para validar o ponto
button.click()
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span[1]')))
button.click()
time.sleep(5)
driver.quit()