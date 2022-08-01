# -*- coding: utf-8 -*-

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색

# Naver검색API에서 제공하는 Python코드를 그대로 활용하여, 검색결과를
# 데이터프레임으로 만든 후 Excel파일로 저장한다.
import os
import sys
import urllib.request
# JSON파싱을 위한 라이브러리 추가
import json
import pandas as pd

# Naver API key는 개발자센터에서 발급받은후 추가한다.
client_id = "lVw5Obaklk0X3zsGiZdL"
client_secret = "pbcj73yIBC"
# 검색어 추가
encText = urllib.parse.quote("JSP책")
# 요청URL : 우리는 JSON결과를 받아서 사용할 예정.
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    # 요청에 성공하면 검색결과를 받아온다.
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
    
# 파싱한 정보를 저장할 리스트를 생성
title = []
bloggername = []
bloggerlink = []
# 콜백데이터를 파싱하기 위해 JSON객체로 로드한다.
json_data = json.loads(result)
# item의 value가 JSON배열이므로 for문으로 반복해서 파싱할 수 있다.
for item in json_data['items']:
    # 제목은 로그로 출력해본다.
    #print(item['title'])
    # 제목, 블로거, 바로가기 링크를 리스트에 추가한다.
    title.append(item['title'])
    bloggername.append(item['bloggername'])
    bloggerlink.append(item['bloggerlink'])
        
# 파싱되어 저장된 데이터로 데이터프레임을 생성한다.
df = pd.DataFrame({'제목':title, '작성자':bloggername, '링크':bloggerlink})
print(df)

# 인덱스를 지정한 후 엑셀로 저장한다.
df.set_index('제목', inplace=True)
df.to_excel("./save/JSP검색결과.xlsx")