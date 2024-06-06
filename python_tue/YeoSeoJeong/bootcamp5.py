from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import time

# 로그인 정보 설정
LMS_ID = 'sjykol'
LMS_PASSWORD = '051221sjy@'

def infinite_scroll(driver, scroll_pause_time=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data = []

try:
    driver.get('https://lms1.knu.ac.kr/')
    
    # 광고나 팝업 닫기
    try:
        popup_close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="xn-popup-wrapper"]/div/div[2]/button'))
        )
        driver.execute_script("arguments[0].click();", popup_close_button)
    except TimeoutException:
        print("팝업이 없습니다. 로그인 진행 중...")
    
    # 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/a'))
    )
    driver.execute_script("arguments[0].click();", login_button)

    # 통합 로그인 버튼 클릭
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[2]/a'))
    )
    driver.execute_script("arguments[0].click();", login_button)

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
    driver.execute_script("arguments[0].click();", login_button)

    # LMS 페이지로 이동
    driver.execute_script("goToLMS()")

    # 무한 스크롤 적용
    infinite_scroll(driver)

    # 페이지 소스 가져오기
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # 데이터를 파싱하여 추출
    days = soup.find_all('div', class_='Day-styles__root planner-day')
    for day in days:
        date_element = day.find('div', class_='cjUyb_bGBk cjUyb_ycrn cjUyb_dfDs cjUyb_eQnG')
        date_text = date_element.text.strip() if date_element else "날짜 없음"

        groupings = day.find_all('div', class_='Grouping-styles__root planner-grouping')

        for grouping in groupings:
            subject_element = grouping.find('span', class_='Grouping-styles__title')
            subject_name = subject_element.text.strip() if subject_element else "과목명 없음"

            type_element = grouping.find('div', class_='PlannerItem-styles__type')
            type_text = type_element.text.strip() if type_element else "유형 없음"
            
            title_element = grouping.find('div', class_='PlannerItem-styles__title')
            title_text = title_element.text.strip() if title_element else "제목 없음"
            
            due_element = grouping.find('div', class_='PlannerItem-styles__due')
            due_text = due_element.text.strip() if due_element else "마감일 없음"
            
            badge_item = grouping.find('li', class_='BadgeList-styles__item')
            badge_text = badge_item.find('span').text.strip() if badge_item else "뱃지 없음"

            data.append({
                'date': date_text,
                'subject_name': subject_name,
                'type_text': type_text,
                'title_text': title_text,
                'due_text': due_text,
                'badge_text': badge_text
            })

except Exception as e:
    print(f"오류 발생: {e}")
    driver.quit()

# Tkinter GUI 설정
root = tk.Tk()
root.title("LMS 데이터")

root.configure(bg='light blue')

style = ttk.Style()
style.configure("Treeview",
                background="light blue",
                fieldbackground="light blue",
                foreground="black",
                font=('Helvetica', 10))
style.configure("Treeview.Heading", background="deep sky blue", foreground="white", font=('Helvetica', 10, 'bold'))

tree = ttk.Treeview(root, columns=('Date', 'Subject Name', 'Type Text', 'Title Text', 'Due Text', 'Badge Text'), show='headings', style="Treeview")
tree.heading('Date', text='날짜')
tree.heading('Subject Name', text='과목명')
tree.heading('Type Text', text='유형')
tree.heading('Title Text', text='제목')
tree.heading('Due Text', text='마감일')
tree.heading('Badge Text', text='뱃지')

tree.pack(fill='both', expand=True, padx=10, pady=10)

xscrollbar = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
xscrollbar.pack(side='bottom', fill='x')
tree.configure(xscrollcommand=xscrollbar.set)

for item in data:
    tree.insert('', 'end', values=(item['date'], item['subject_name'], item['type_text'], item['title_text'], item['due_text'], item['badge_text']))

root.mainloop()