# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('./data/chromedriver.exe')
# 웹페이지가 로드될떄까지 명시적으로 대기한다.
driver.implicitly_wait(3)
# 네이버 로그인 페이지로 접속한다.
url = 'http://nid.naver.com/nidlogin.login'
driver.get(url)

'''
단일 엘리먼트에 접근하기 위한 메서드
find_element_by_name(name속성명)
find_element_by_id(id속성명)
find_element_by_xpath(xpath경로)
find_element_by_css_selector(셀렉터)
find_element_by_class_name(class속성명)
find_element_by_tag_name(HTML태그명)

복수 엘리먼트에 접근하려면 위 메서드의 element에 s를 붙여주면된다.
find_elements_by_css_selector(셀렉터)
'''
# send_keys() : <input> 태그에 지정한 값을 입력해준다.
driver.find_element_by_name('id').send_keys('madcatz92')
driver.find_element_by_name('pw').send_keys('wnsl458#')
# xpath로 지정한 엘리먼트를 클릭한다. 즉 로그인 버튼을 누른다.
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="log.login"]').click()