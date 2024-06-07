import requests
from bs4 import BeautifulSoup

# 멜론 차트 페이지 URL
URL = 'https://www.melon.com/chart/index.htm'

# HTTP 헤더 설정 (웹 크롤링 방지를 피하기 위해 브라우저처럼 보이도록 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 웹 페이지 요청
response = requests.get(URL, headers=headers)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목들을 담을 리스트
song_titles = []

# 멜론 차트의 노래 제목을 선택하는 CSS 선택자
title_selector = 'div.ellipsis.rank01 > span > a'

# CSS 선택자를 사용하여 제목 요소들 찾기
title_elements = soup.select(title_selector)

# 각 제목 요소에서 텍스트 추출
for title_element in title_elements:
    song_titles.append(title_element.get_text(strip=True))

# 추출한 노래 제목들 출력
for idx, title in enumerate(song_titles, 1):
    print(f"{idx}. {title}")
