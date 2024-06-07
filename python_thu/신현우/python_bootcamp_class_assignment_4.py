import requests
import bs4

URL = 'https://sports.news.naver.com/kbaseball/record/index?category=kbo'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'tbl_box'})
# print(target)
teams = target.find_all("td", {'class' : 'tm'})

print("KBO 팀 순위")
for team in teams:
    print(team.text)
    
    

    
