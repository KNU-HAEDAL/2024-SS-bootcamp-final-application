import requests
import bs4


URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)
''''' #당첨번호가 포함된 부분 긁어오기
target = '<div class="nums">'

if target in raw.text:
    idx = raw.text.index(target)
    print(raw.text[idx:idx + 578])
'''
html = bs4.BeautifulSoup(raw.text, 'html.parser')
#print(type(raw.text)) ->str
#print(type(html)) -> bs4.beautifulsoup

target = html.find('div', {'class' : 'nums'})
#print(target) #위 주석과달리 열이 안맞춰져있게 한줄로출력

balls = target.find_all("span", {'class' : 'ball_645'})
#target중 span긁어오기


for ball in balls:
    #print(ball) #span문 전체 긁어오기
    print('당첨번호 : ',ball.text) #span문 중 숫자만 긁어오기
