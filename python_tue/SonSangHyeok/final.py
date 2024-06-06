from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import time
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

# 로그인 정보 설정
# with open('셀레니움/secret.json') as f:
#     secrets = json.loads(f.read())
# LMS_ID = secrets["LMS_ID"]
# LMS_PASSWORD = secrets["LMS_PW"]

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
    id_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="idpw_id"]'))
    )
    id_input.send_keys("ssh8364")
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="idpw_pw"]'))
    )
    password_input.send_keys("#Sh143143143")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-login"]'))
    )
    login_button.click()

    # 4. lms로 이동하는 자바스크립트 함수 실행
    driver.execute_script("goToLMS()")

    # 페이지 로딩 대기
    time.sleep(3)

    # 스크롤을 위해 페이지 높이 계산
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("""
        var event = new WheelEvent('wheel', {
            deltaY: -1000,
            deltaX: 0,
            bubbles: true
            });
            document.dispatchEvent(event);
        """)
    
        # AJAX 요청이 완료될 때까지 대기
        time.sleep(3)

        # 위로 스크롤 (페이지 맨 위로 스크롤하려면)
        driver.execute_script("window.scrollTo(0, 0);")

        # 스크롤 후 대기 (콘텐츠 로딩 대기)
        time.sleep(3)

        # 새로운 페이지 높이 계산
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 새로운 콘텐츠가 로딩되지 않으면 종료
        if new_height == last_height:
            break

        last_height = new_height

    # 5. 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(page_source, 'html.parser')
    
    days = soup.find_all('div', class_='Day-styles__root planner-day')
    for day in days:
        date_element = day.find('div', class_='cjUyb_bGBk cjUyb_ycrn cjUyb_dfDs cjUyb_eQnG')
        date_text = date_element.text.strip() if date_element else "No date"

        groupings = day.find_all('div', class_='Grouping-styles__root planner-grouping')
        for grouping in groupings:
            subject_element = grouping.find('span', class_='Grouping-styles__title')
            subject_name = subject_element.text.strip() if subject_element else "No subject name"

            type_element = grouping.find('div', class_='PlannerItem-styles__type')
            type_text = type_element.text.strip() if type_element else "No type text"
            
            title_element = grouping.find('div', class_='PlannerItem-styles__title')
            title_text = title_element.text.strip() if title_element else "No title text"
            
            due_element = grouping.find('div', class_='PlannerItem-styles__due')
            due_text = due_element.text.strip() if due_element else "No due text"
            
            badge_item = grouping.find('li', class_='BadgeList-styles__item')
            badge_text = badge_item.find('span').text.strip() if badge_item else "No badge"

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

# 6. Tkinter GUI 설정
root = tk.Tk()
root.title("LMS Data")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", background="gainsboro", foreground="white", font=("Arial", 12, "bold"), padding=(10, 5))

tree = ttk.Treeview(root, columns=('Date', 'Subject Name', 'Type Text', 'Title Text', 'Due Text', 'Badge Text'), show='headings')
tree.heading('Date', text='Date')
tree.heading('Subject Name', text='Subject Name')
tree.heading('Type Text', text='Type Text')
tree.heading('Title Text', text='Title Text')
tree.heading('Due Text', text='Due Text')
tree.heading('Badge Text', text='Badge Text')

tree.pack(fill='both', expand=True)

for item in data:
    tree.insert('', 'end', values=(item['date'], item['subject_name'], item['type_text'], item['title_text'], item['due_text'], item['badge_text']))

scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')
tree.pack(side='left', fill='both', expand=True)

root.mainloop()
