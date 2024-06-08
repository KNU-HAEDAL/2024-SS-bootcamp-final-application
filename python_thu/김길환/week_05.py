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

# 'my_papago.csv' 파일을 읽어서 이미 번역된 영단어를 세트에 저장
try:
    with open('./my_papago.csv', 'r', newline='') as f:
        rdr = csv.reader(f)
        translated_words = set(row[0] for row in rdr if row)
except FileNotFoundError:
    translated_words = set()

# 'my_papago.csv' 파일을 생성하거나 추가 모드로 열기
f = open('./my_papago.csv', 'a', newline='')

# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)

# 열 제목 작성 (파일이 비어 있을 때만)
if not translated_words:
    wtr.writerow(['영단어', '번역결과'])

# 반복문 작성
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break
    # 이미 번역된 영단어인지 확인
    if keyword in translated_words:
        print(f"{keyword}은(는) 이미 번역된 영단어입니다.")
        continue

    # 영단어 입력, 번역 버튼 클릭
    form = driver.find_element(By.CSS_SELECTOR, 'textarea#txtSource')
    form.send_keys(keyword)

    button = driver.find_element(By.CSS_SELECTOR, 'button#btnTranslate')
    button.click()
    time.sleep(1)

    # 번역 결과 저장
    output = driver.find_element(By.CSS_SELECTOR, 'div#txtTarget').text

    # my_papago.csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])

    # 번역된 영단어를 세트에 추가
    translated_words.add(keyword)

    # 영단어 입력 칸 초기화
    form.clear()

# 파일 닫기
f.close()
driver.quit()
