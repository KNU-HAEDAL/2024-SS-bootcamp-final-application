from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import csv

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 우리가 컨트롤 할 수 있는 브라우저가 실행이된다.

driver.get("https://papago.naver.com/")
time.sleep(3)

question = input("번역 할 영단어를 입력하세요. : ")
form = driver.find_element(By.CSS_SELECTOR,"textarea#txtSource")
form.send_keys(question)

button = driver.find_element(By.CSS_SELECTOR,"button#btnTranslate")
button.click()

time.sleep(5)
result = driver.find_element(By.CSS_SELECTOR,"div#txtTarget")
print(question, "->", result.text)

driver.close()