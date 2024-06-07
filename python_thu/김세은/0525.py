from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import csv

from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 설정 및 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://papago.naver.com/")
time.sleep(3)

# 기존 'my_papago.csv' 파일을 읽고 저장된 영단어를 set으로 저장
existing_words = set()
try:
    with open('./my_papago.csv', 'r', newline='') as f:
        rdr = csv.reader(f)
        next(rdr)  # 헤더 건너뛰기
        for row in rdr:
            existing_words.add(row[0])
except FileNotFoundError:
    pass

# 'my_papago.csv' 파일을 쓰기 모드로 열기
with open('./my_papago.csv', 'a', newline='') as f:
    wtr = csv.writer(f)
    
    # 파일이 처음 생성된 경우 열 제목 작성
    if not existing_words:
        wtr.writerow(['영단어', '번역결과'])
    
    # 번역 작업 반복
    while True:
        keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
        if keyword == '0':
            print('번역 종료')
            break
        
        # 중복 단어 체크
        if keyword in existing_words:
            print(f"'{keyword}'는 이미 번역된 단어입니다.")
            continue
        
        # 영단어 입력 및 번역 버튼 클릭
        form = driver.find_element(By.CSS_SELECTOR, 'textarea#txtSource')
        form.send_keys(keyword)

        button = driver.find_element(By.CSS_SELECTOR, 'button#btnTranslate')
        button.click()
        time.sleep(3)  # 번역 결과가 나올 때까지 대기

        # 번역 결과 가져오기
        output = driver.find_element(By.CSS_SELECTOR, 'div#txtTarget').text
        
        # 번역 결과를 CSV 파일에 저장
        wtr.writerow([keyword, output])
        existing_words.add(keyword)
        
        # 영단어 입력 칸 초기화
        form.clear()

# 브라우저 종료
driver.quit()
