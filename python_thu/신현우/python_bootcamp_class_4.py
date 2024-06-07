import requests 
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL) # 스크립트 전체를 따옴.

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('g', {'class' : 'nums'})

balls = target.find_all("text",{'class':'bb-shape'})

for ball in balls:
    print("당첨번호 : ",ball.text)
    
    
    
    
#target = '<div class="nums">'
#print(raw)
#print(raw.text)
# 출력값 Response [200]
# <Response [200]>은 get 함수를 통해 보낸 요청이 정상적으로 처리되었다는 의미에요.

#if target in raw.text:
#    idx = raw.text.index(target)
#    print(raw.text[idx:idx + 578])
    
