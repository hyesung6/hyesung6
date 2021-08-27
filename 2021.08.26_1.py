"""
selenium 모듈 필요
- 웹 브라우저 자동화를 위한 라이브러리
- 컨텐츠에 입력, 클릭, 가져오기 등이 가능하다
"""

from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

# url = 'https://www.naver.com'
# driver.get(url)

url = 'https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'
driver.get(url)

# 사이트에 올라오는 게시글들을 모아서 특정 키워드를 뽑아내는 등에 사용이 가능하다.
# 어떤 키워드로 게시글이 많이 쓰여졌는지..
# 페이지 정보가 주소에 노출되는 게시글들은 간단하다. 주소창에 lis01, lis02, lis03 ... 등으로 이어질 경우

print('='*40)

driver.get(url)

# selenium 은 웹 페이지의 css선택자를 통하여 색인할 수 있는 기능이 있다
# driver.find_~~~ 여러가지가 있는데 어떤 키워드로 요소를 찾아낼지는 취향대로

selected_selector = driver.find_element_by_css_selector('li.pclist_list_tit42')
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selector.click()       # css로 구현된 링크에 접속(클릭하듯)하는 함수
# click() 페이지 이동을 권장하지 않음 DOM 을 사용할 수 없기 때문

# from

# selected_query.send_keys(Keys.ENTER)

# 보안 상의 이유로 대개 웹 페이지에 script를 사용하는 건 막혀있다
# url = 'http://example.com'
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get(url)
# driver.execute_script("alert('wow')")

print('='*40)

from bs4 import BeautifulSoup

url = 'http://example.com'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.select('div'))


# 도전 과제 - 파이썬 환경에서 terms.naver.com에 접속해 '빅데이터' 검색하여 나오는 결과를 출력하기