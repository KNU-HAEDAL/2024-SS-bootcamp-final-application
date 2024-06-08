import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%9D%A0%EB%B3%84%20%EC%9A%B4%EC%84%B8"


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


monkey_fortune = soup.select_one("body > div:nth-of-type(3) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(1) > div > div > ul:nth-of-type(2) > li:nth-of-type(9) > p")


if monkey_fortune:
    fortune_text = monkey_fortune.get_text(strip=True)
    print(f"오늘의 원숭이띠 운세: {fortune_text}")
else:
    print("운세 정보를 찾을 수 없습니다.")
