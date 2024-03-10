from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.investing.com/equities/apple-computer-inc-commentary")
time.sleep(2)
action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()

div_element = driver.find_element(By.ID,"comments")
contenido = div_element.text
print(str(contenido))

with open("datosinvesting.txt","w", encoding='utf-8') as file:
    file.write(contenido)