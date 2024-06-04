from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import ttk
import tkinter as tk
import json
import time


# 로그인 정보
with open('5,6/secret.json') as f:
    secrets = json.loads(f.read())
LMS_ID = secrets["LMS_ID"]
LMS_PASSWORD = secrets["LMS_PASSWORD"]

# WebDriver
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # (이전에 나오는 크롬 창들을 안보이게 해줌GUI 없이 실행, 디버깅할 때는 주석 처리
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data = []

try:
    #LMS 로그인 페이지 열기
    driver.get('https://lms1.knu.ac.kr/')


    # 1. 로그인 버튼 클릭
    #WebDriverWait(driver, 10) -> 
    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/a'))
    )

    driver.execute_script("arguments[0].click();", login_button) #자바스크립트로 클릭한 효과
    # login_button.click() #-> 팝업창 때문에 못씀


    
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



    # 4. 나의과목 바로가기 버튼 클릭(팝업창 때문에 4-1사용)
    # login_button2 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="visual"]/div/div[2]/div[2]/div[1]'))
    # )
    # driver.execute_script("arguments[0].click();", login_button2)


    # 4-1.lms로 이동하는 자바스크립트 함수 실행
    driver.execute_script("goToLMS()")

    ## new activity
    for _ in range(30):
        try:
            new_button = WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="new_activity_button"]'))
            )
            new_button.click()
            time.sleep(1)  # 클릭 간격을 1초로 설정
                
        except Exception as e:
            print(f"Failed to click the NEW button: {e}")
            break

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
    driver.quit()

print(data)


# Tkinter GUI 설정
root = tk.Tk()
root.title("LMS Data")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# 스타일 설정
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background="#4caf50", foreground="white")
style.configure("Treeview", font=('Helvetica', 10), background="#f0f0f0", foreground="black", rowheight=25)
style.map("Treeview", background=[('selected', '#347083')], foreground=[('selected', 'white')])

# Frame 설정
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True, padx=20, pady=20)

# Treeview 설정
tree = ttk.Treeview(frame, columns=('Date', 'Subject Name', 'Type Text', 'Title Text', 'Due Text', 'Badge Text'), show='headings', selectmode="browse")
tree.heading('Date', text='Date')
tree.heading('Subject Name', text='Subject Name')
tree.heading('Type Text', text='Type Text')
tree.heading('Title Text', text='Title Text')
tree.heading('Due Text', text='Due Text')
tree.heading('Badge Text', text='Badge Text')

# 컬럼 너비 설정
tree.column('Date', width=100)
tree.column('Subject Name', width=150)
tree.column('Type Text', width=100)
tree.column('Title Text', width=200)
tree.column('Due Text', width=100)
tree.column('Badge Text', width=100)

# 스크롤바 설정
scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

tree.pack(fill='both', expand=True)

# 데이터 삽입
for item in data:
    tags = ()
    if '제출됨' in item['badge_text']:
        tags = ('submitted',)
    tree.insert('', 'end', values=(item['date'], item['subject_name'], item['type_text'], item['title_text'], item['due_text'], item['badge_text']), tags=tags)

# 스타일 추가
tree.tag_configure('submitted', background='#d4fcd4')

# 애플리케이션 실행
root.mainloop()