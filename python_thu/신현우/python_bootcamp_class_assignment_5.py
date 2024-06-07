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

# 'my_papago.csv' 파일을 읽어서 기존 영단어 목록을 저장할 집합 생성
existing_words = set()
try:
    with open('./my_papago.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        for row in reader:
            existing_words.add(row[0])
except FileNotFoundError:
    # 파일이 없을 경우, 기존 단어 목록은 빈 집합으로 유지
    pass

# 'my_papago.csv' 파일을 생성하여 변수 'f'에 저장
f = open('./my_papago.csv', 'a', newline='')  # 추가 모드로 파일 열기

# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)

# 열 제목 작성 (파일이 존재하지 않는 경우에만 헤더 작성)
if len(existing_words) == 0:
    wtr.writerow(['영단어', '번역결과'])

# 반복문 작성
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break
    
    # 영단어가 기존 목록에 없을 경우에만 번역 및 저장 수행
    if keyword not in existing_words:
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
        existing_words.add(keyword)  # 새로 번역한 단어는 목록에 추가
        
        # 영단어 입력 칸 초기화
        driver.find_element(By.CSS_SELECTOR, 'textarea#txtSource').clear()
    else:
        print(f"'{keyword}'는 이미 번역된 단어입니다.")

# 파일 닫기
f.close()

# 브라우저 종료
driver.quit()