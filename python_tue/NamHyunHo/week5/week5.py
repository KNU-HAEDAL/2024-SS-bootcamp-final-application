from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import time

# 로그인 정보 설정
with open('./secret.json') as f:
    secrets = json.loads(f.read())
LMS_ID = secrets["LMS_ID"]
LMS_PASSWORD = secrets["LMS_PW"]

# WebDriver 설정
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # GUI 없이 실행, 디버깅할 때는 주석 처리
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data = []

try:
    # 경북대학교 LMS 로그인 페이지 열기
    driver.get('https://lms1.knu.ac.kr/')

    # 1. 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/a'))
    )
    driver.execute_script("arguments[0].click();", login_button)
    
    # 2. 통합 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[2]/a'))
    )
    login_button.click()
    
    # 3. 로그인
    # ID 입력
    id_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="idpw_id"]'))
    )
    id_input.send_keys(LMS_ID)
    # 비밀번호 입력
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="idpw_pw"]'))
    )
    password_input.send_keys(LMS_PASSWORD)
    # 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-login"]'))
    )
    login_button.click()
    
    # 4. 나의과목 바로가기 버튼 클릭
    driver.execute_script("goToLMS()")

    # 위로 스크롤 하기
    while True:
        specific_selector = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="new_activity_button"]'))
        )
        specific_selector.click()
        time.sleep(2)
        
        try:
            scroll_end_text = driver.find_element(By.XPATH, '//*[@id="dashboard-planner"]/div/div[1]/div/div[2]')
            if scroll_end_text.is_displayed():
                break
        except:
            continue

    # 5. 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    
    days = soup.find_all('div', class_='Day-styles__root planner-day')
    for day in days:
        # 날짜 정보 추출
        date_element = day.find('div', class_='cjUyb_bGBk cjUyb_ycrn cjUyb_dfDs cjUyb_eQnG')
        date_text = date_element.text.strip() if date_element else "No date"

        # 해당 날짜의 각 그룹 찾기
        groupings = day.find_all('div', class_='Grouping-styles__root planner-grouping')

        for grouping in groupings:
            # 과목 이름 추출
            subject_element = grouping.find('span', class_='Grouping-styles__title')
            subject_name = subject_element.text.strip() if subject_element else "No subject name"

            # class="PlannerItem-styles__type" 내부의 텍스트 추출
            type_element = grouping.find('div', class_='PlannerItem-styles__type')
            type_text = type_element.text.strip() if type_element else "No type text"
            
            # class="PlannerItem-styles__title" 안의 텍스트 추출
            title_element = grouping.find('div', class_='PlannerItem-styles__title')
            title_text = title_element.text.strip() if title_element else "No title text"
            
            # class="PlannerItem-styles__due" 내부의 텍스트 추출
            due_element = grouping.find('div', class_='PlannerItem-styles__due')
            due_text = due_element.text.strip() if due_element else "No due text"
            
            # class="BadgeList-styles__item"의 존재 여부와 내부의 텍스트 추출
            badge_item = grouping.find('li', class_='BadgeList-styles__item')
            badge_text = badge_item.find('span').text.strip() if badge_item else "No badge"

            # 데이터를 리스트에 저장
            data.append({
                'date': date_text,
                'subject_name': subject_name,
                'type_text': type_text,
                'title_text': title_text,
                'due_text': due_text,
                'badge_text': badge_text
            })

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

print(data)

# 6. Tkinter GUI 설정
root = tk.Tk()
root.title("LMS Data")

# Treeview 설정
tree = ttk.Treeview(root, columns=('Date', 'Subject Name', 'Type Text', 'Title Text', 'Due Text', 'Badge Text'), show='headings')
tree.heading('Date', text='Date')
tree.heading('Subject Name', text='Subject Name')
tree.heading('Type Text', text='Type Text')
tree.heading('Title Text', text='Title Text')
tree.heading('Due Text', text='Due Text')
tree.heading('Badge Text', text='Badge Text')

tree.pack(fill='both', expand=True)

# 데이터 삽입
for item in data:
    tree.insert('', 'end', values=(item['date'], item['subject_name'], item['type_text'], item['title_text'], item['due_text'], item['badge_text']))

root.mainloop()
