# -*- coding: utf-8 -*-

# 셀레니움을 임포트 한다.
from selenium import webdriver
# 크롬 드라이버를 로드한다. 이때 웹브라우저가 실행된다.
driver = webdriver.Chrome('./data/chromedriver.exe')
# 만약 위에서 실행이 되지 않는다면 라이브버리 설치와 드라이버의 경로를 확인한다.
 
# 멜론 실시간 차트 페이지로 접속하여 페이지정보(HTML)를 얻어온다.
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

# 뷰티플숩을 실행한다. html.parser를 로드한다.
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보를 저장할 리스트 생성
song_data = []
rank = 1
# 셀렉터를 이용해서 반복되는 원소(차트)를 가져온다.
songs = soup.select('tbody > tr')
for song in songs:
    # 노래제목
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    # 가수
    singer = song.select('div.ellipsis.rank02 > a')[0].text
    # 콘솔 출력시 |를 구분자로 사용
    print(title, singer, sep="|")
    # 파싱한 정보는 리스트에 저장한다.
    song_data.append(['Melon', rank, title, singer])
    rank += 1

# 리스트에 저장된 내용을 데이터프레임으로 변환하고 엑셀로 저장한다.
import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
# 데이터프레임의 상위 5개 행을 출력한다.
print(pd_data.head())
pd_data.to_excel('./save/melon.xlsx', index=False)