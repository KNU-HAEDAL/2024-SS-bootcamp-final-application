import requests
import bs4
import unicodedata

def preFormat(string, width, align='<', fill=' '):
    count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in string))
    return {
        '>': lambda s: fill * count + s, # lambda 매개변수 : 표현식
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2)
                       + s
                       + fill * (count / 2 + count % 2)
    }[align](string)


URL = 'https://finance.naver.com/sise/' #네이버 증권 사이트
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')
domesticStocks = html.find('table', {'summary' : '탑종목 시가총액상위 리스트'})
a = html.get_text
topStocks = domesticStocks.find_all('tr')

topStocks = topStocks[2:15]
del topStocks[5:8]

print("<<국내 탑종목 시가총액상위 리스트>>")
print("---------------------------------------------")
print("%s %8s %9s %4s %4s"%("순위", "종목명", "현재가", "전일비", "등락률"))
print("---------------------------------------------")

cnt = 1
for stock in topStocks:
    stockData = stock.find_all('td')
    item = stockData[1].text
    cur_price = stockData[2].text
    difference = ""
    dailyChange = stockData[3].find_all('span')
    
    if dailyChange[0].text == "상승":
        difference = '+' + dailyChange[1].text.strip()
    elif dailyChange[0].text == "하락":
        difference = '-' + dailyChange[1].text.strip()
    difference.replace(" ", "")
    fluc_rate = stockData[4].text.strip()
    
    print("[%2d] %s %7s  %-6s  %5s"%(cnt, preFormat(item, 16), cur_price, difference, fluc_rate))
    cnt += 1
  
