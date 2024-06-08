from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import csv

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://papago.naver.com/")
time.sleep(3)

words_set = set()

with open('my_papago.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['입력 단어', '번역 결과']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        word = input("번역 할 영단어를 입력하세요. (종료하려면 'exit' 입력) : ")

        if word.lower() == 'exit':
            break

        if word.lower() in words_set:
            print(f"{word}는 이미 번역되었습니다.")
            continue

        form = driver.find_element(By.CSS_SELECTOR, "#txtSource")
        form.clear()
        form.send_keys(word)

        button = driver.find_element(By.CSS_SELECTOR, "#btnTranslate")
        button.click()

        time.sleep(2)

        result = driver.find_element(By.CSS_SELECTOR, "#txtTarget").text

        words_set.add(word.lower())
        print(f"{word} -> {result}")

        writer.writerow({'입력 단어': word, '번역 결과': result})

driver.close()