# -*- coding: utf-8 -*-

# 특정 URL로의 요청을 통해 페이지의 정보(HTML)를 읽어온다.
from bs4 import BeautifulSoup
# 읽어온 정보에서 정보를 파싱한다.
import requests
import pandas as pd

# 크롤링할 url(네이버 지식인)
url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
# request 라이브러리를 통해 접속해서 HTML코드를 받아온다.
response = requests.get(url)

# 파싱한 정보를 저장하기 위해 딕셔너리 객체 생성
dicts = {}

# 요청에 성공한 경우라면 파싱을 진행한다.
if response.status_code==200:
    # 얻어온 정보를 파싱하기 위해 soup객체로 변환한다.
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # 첫번째 제목을 가져와서 출력한다. 이떄 선택자는 개발자 도구의 
    # 셀렉터 복사 기능을 사용한다.
    title01 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt')
    #print("첫번째제목(HTML코드포함):", title01)
    
    # 태그를 제거한 후 텍스트만 얻어올때는 get_text()를 사용한다.
    text01 = title01.get_text()
    #print("첫번째제목(텍스트만추출):", text01)
    
    # 반복되는 원소내에서 텍스트만 추출하여 딕셔너리로 만든다.
    ul = soup.select_one('#s_content > div.section > ul')
    #print(ul) -- print문으로 중간중간 확인하면서 가야한다.
    title02 = ul.select('li > dl > dt > a')
    #print(title02)
    
    # 검색된 제목의 갯수만큼 반복하여 텍스트를 추출한다.
    cnt = 1
    for tit in title02:
        #print(tit.get_text())
        #  크롤링한 순서대로 항목1~10까지 문자열을 생성한다.
        # Python에서는 문자열과 숫자를 연결할때 str()함수로 숫자를 문자로
        # 변경한 후 연결해야 한다.
        my_key = '항목'+ str(cnt)
        # 크롤링한 정보를 딕셔너리로 저장한다.
        # 이떄 key로 '항목N'를 사용하고, value로 크롤링한 정보를 사용한다.
        dicts[my_key] = [tit.get_text(), '2행데이터'];
        # cnt를 1증가시킨다. Python은 증감연산자가 없다.
        cnt += 1
    print(dicts)
else:
    # 요청에 실패했다면 응답코드를 출력한다.
    print(response.status_code) 
    
# 딕셔너리를 데이터프레임으로 변환한다.
df = pd.DataFrame(dicts)
print(df)
    