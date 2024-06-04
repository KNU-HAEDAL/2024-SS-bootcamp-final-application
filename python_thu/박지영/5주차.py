from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Setup the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://papago.naver.com/")
time.sleep(3)

# Load the existing translations from the CSV file
try:
    with open('./my_papago.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        existing_translations = {rows[0]: rows[1] for rows in reader}
except FileNotFoundError:
    existing_translations = {}

# Open the CSV file in append mode
f = open('./my_papago.csv', 'a', newline='')
wtr = csv.writer(f)

# Write the header only if the file was empty
if not existing_translations:
    wtr.writerow(['영단어', '번역결과'])

# Main loop for translation
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break

    # Check if the keyword is already translated
    if keyword in existing_translations:
        print(f"'{keyword}'는 이미 번역되었습니다: {existing_translations[keyword]}")
        continue

    # Translate the keyword
    form = driver.find_element(By.CSS_SELECTOR, 'textarea#txtSource')
    form.send_keys(keyword)

    button = driver.find_element(By.CSS_SELECTOR, 'button#btnTranslate')
    button.click()
    time.sleep(1)

    # Get the translation result
    output = driver.find_element(By.CSS_SELECTOR, 'div#txtTarget').text

    # Save the new translation
    wtr.writerow([keyword, output])
    existing_translations[keyword] = output

    # Clear the input field
    form.clear()

# Close the file and the browser
f.close()
driver.quit()
