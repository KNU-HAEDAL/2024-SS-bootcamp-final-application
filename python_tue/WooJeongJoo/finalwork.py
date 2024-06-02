from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import json
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time
from selenium.webdriver.common.keys import Keys


# 로그인 정보 설정
with open('./secret.json') as f:
    secrets = json.loads(f.read())
LMS_ID = secrets["LMS_ID"]
LMS_PASSWORD = secrets["LMS_PASSWORD"]

def infinite_scroll(element, scroll_pause_time=1):
    last_height = driver.execute_script("return arguments[0].scrollHeight", element)
    
    while True:
        # 스크롤 다운
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
        
        # 대기 시간
        time.sleep(scroll_pause_time)
        
        # 새로운 스크롤 높이 계산
        new_height = driver.execute_script("return arguments[0].scrollHeight", element)
        
        # 스크롤이 끝에 도달했는지 확인
        if new_height == last_height:
            break
        last_height = new_height

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
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/a'))
    )
    driver.execute_script("arguments[0].click();", login_button)
    # login_button.click()

    
    # 2. 통합 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[2]/a'))
    )
    login_button.click()
    

	# 3. 로그인
    # ID 입력
    id_input = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="idpw_id"]'))
    )
    id_input.send_keys(LMS_ID)
    # 비밀번호 입력
    password_input = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="idpw_pw"]'))
    )
    password_input.send_keys(LMS_PASSWORD)
    # 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="btn-login"]'))
    )
    login_button.click()

    
    # 4. 나의과목 바로가기 버튼 클릭
    # login_button2 = WebDriverWait(driver, 10).until(
    #     expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/div[1]'))
    # )
    # driver.execute_script("arguments[0].click();", login_button2)

    # # 4-1.lms로 이동하는 자바스크립트 함수 실행
    driver.execute_script("goToLMS()")
    # new_activity = WebDriverWait(driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="new_activity_button"]'))
    #     )
    

    # new_activity = WebDriverWait(driver, 10).until(
    #     expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="new_activity_button"]'))
    #     )
    # new_activity.click()

    while True:
        try:
            # 요소가 클릭 가능할 때까지 대기
            new_activity = WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="new_activity_button"]'))
            )
            # 요소 클릭
            new_activity.click()
            print("Element clicked successfully.")
            time.sleep(3)
        except TimeoutException:
        # 요소를 찾지 못했을 때 예외 처리
            print("Element not found, retrying...")
        try:
            driver.find_element(By.XPATH, '//*[@id="new_activity_button"]')
        except NoSuchElementException:
            print("Element no longer exists. Exiting loop.")
            break  # 요소가 존재하지 않으면 루프 종료

    time.sleep(5)
    
    # 5. 페이지 소스 가져오기
    waitasec = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="dashboard-planner"]/div/div[1]/div/div[1]'))
    )
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
    driver.quit()

# print(data)


# 6. Tkinter GUI 설정
root = ThemedTk(theme="blue")
root.title("LMS Data")


# Treeview 설정 == 표 형식
tree = ttk.Treeview(root, columns=('Date', 'Subject Name', 'Type Text', 'Title Text', 'Due Text', 'Badge Text'), show='headings')
tree.heading('Date', text='Date', anchor="center")
tree.heading('Subject Name', text='Subject Name', anchor="center")
tree.heading('Type Text', text='Type Text', anchor="center")
tree.heading('Title Text', text='Title Text', anchor="center")
tree.heading('Due Text', text='Due Text', anchor="center")
tree.heading('Badge Text', text='Badge Text', anchor="center")
tree.tag_configure('date', background="white")

tree.pack(fill='both', expand=True)

# 데이터 삽입
for item in data:
    tree.insert('', 'end', values=(item['date'], item['subject_name'], item['type_text'], item['title_text'], item['due_text'], item['badge_text']))

root.mainloop()