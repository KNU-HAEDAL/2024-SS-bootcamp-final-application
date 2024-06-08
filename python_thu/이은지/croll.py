import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    URL = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        chart = soup.find('tbody').find_all('tr')

        melon_chart = []
        for song in chart:
            rank = song.find('span', {'class': 'rank'}).text
            title = song.find('div', {'class': 'ellipsis rank01'}).find('a').text.strip()
            artist = song.find('div', {'class': 'ellipsis rank02'}).find('a').text.strip()
            melon_chart.append({'rank': rank, 'title': title, 'artist': artist})

        return melon_chart

# 실행
chart = get_melon_chart()
if chart:
    for song in chart:
        print(f"{song['rank']}위 : {song['title']} - {song['artist']}")