from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 우리가 컨트롤 할 수 있는 브라우저가 실행이된다.

driver.get("https://www.naver.com")

driver.find_element(By.ID, 'query').send_keys("날씨", Keys.ENTER)



time.sleep( 3 )

word = driver.find_element(By.CLASS_NAME, 'temperature_text').text
print(word.split("\n")[1]) #현재기온을 찾아 출력

# 브라우저를 닫으라는 요청이 있을 때 까지 페이지 닫기지 않게 설정
#input("브라우저를 닫기 위해 엔터키를 누르세요.")  
driver.quit()  #브라우저 닫기