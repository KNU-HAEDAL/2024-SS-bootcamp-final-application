import requests
import bs4

# URL 설정
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=GDP%EC%88%9C%EC%9C%84&oquery=GDP%EC%88%9C%EC%9C%84&tqi=iDx7KdqVN8wsscApJkwssssssFZ-442814"
raw = requests.get(url)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find_all('div', {'class':'info'})

for i, info in enumerate(target[:5], start=1):
    country = info.find('span', {'class': 'text'}).get_text(strip=True)
    print(f"{i}위: {country}")
