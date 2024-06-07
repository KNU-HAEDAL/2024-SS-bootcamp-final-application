import requests
from bs4 import BeautifulSoup as bs
from random import sample
import sys
import os
import re
# import keyword_naitive
# import crawling.keyword_naitive as keyword_naitive

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from huggingface import summarize_context
# from summarize.huggingface import summarize_context


headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0', 
        # 어떤 운영체제 쓰고 있느니 표기
    }
)

category_dict = {
    '정치': '100',
    '경제': '101',
    '사회': '102',
    '생활/문화': '103',
    '세계': '104',
    'IT/과학': '105'
}


def get_category_headlines(category: str):

    # 페이지 가져오기
    categories = list(category_dict)
    category_code = category_dict[category]
    base_url = "https://news.naver.com/section/"

    response = requests.get(f"{base_url}{category_code}", headers=headers)
    html_text = response.text

    # 헤드라인 추출
    soup = bs(html_text, 'html.parser')
    pattern = re.compile('_SECTION_HEADLINE_LIST_.*')
    news_headlines_container = soup.find(id=pattern)
    news_items = news_headlines_container.find_all('div', class_='sa_item_inner')


    for item in news_items:
        title = item.find('strong', class_='sa_text_strong').text.strip()
        link = item.find('a')['href'].strip()

        img_tag = item.find('img')
        img_url = img_tag['data-src'].strip() # 이미지 URL 가져오기
        print(img_url)

        
        print(f'title: {title}')
        print(f'link: {link}')
        print(f"img_url: {img_url}")
        print('==========================================================================================')
        print()



    news = []

    return news


get_category_headlines('경제')
