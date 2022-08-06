# -*- coding: utf-8 -*-

# 라이브러리 임포트
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# 셀레니움 드라이버 로드 및 크롬브라우저 열기
driver = webdriver.Chrome('./data/chromedriver.exe')
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

# 페이지 정보를 얻어와서 숩 객체 생
html = driver.page_source
soup = BeautifulSoup()(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('tbody > tr')
for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    print(title, singer, sep="|")
    song_data.append(['Genie', rank, title, singer])
    rank += 1
    
# 두번째 페이지
driver.implicitly_wait(2) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.find_element_by_xpath(
    '//*[@id="body-content"]/div[7]/a[2]'
).click()
# 세번째 페이지
driver.implicitly_wait(2) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.find_element_by_xpath(
    '//*[@id="body-content"]/div[7]/a[3]'
).click()
# 네번째 페이지
driver.implicitly_wait(2) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.find_element_by_xpath(
    '//*[@id="body-content"]/div[7]/a[4]'
).click()

songs = soup.select('tbody > tr')
for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    print(title, singer, sep="|")
    song_data.append(['Genie', rank, title, singer])
    rank += 1
    
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel('./save/genie.xlsx', index=False)