import bs4

# beautifulsoup은 웹페이지 코드의 <>'tag 부분을 알아서 해석해준다.
# 웹 브라우저가 Parsing 하듯이..


"""
파이썬에서 많이 사용하는 parser

1) lxml : xml(eXtensible Markup Language) 해석이 가능한 Parser. 파이썬 2.x, 3,x 모두 지원
-- 기존의 HTML은 명명되지 않은 태그를 사용하면 인식되지 않아서, 임의의 태그에 기능을 부여하려고 개발된 것이 XML
-- 상대적으로 다른 Parser에 비해 빠름 (c 기반)

2) html5lib : 웹 브라우저 방식으로 HTML 해석
-- lxml과 비교하면 상대적으로 느림

3) html.parser : html5lib과 거의 비슷
"""

from bs4 import BeautifulSoup

html = '''<p>test</p>'''
print(html)
soup = BeautifulSoup(html, 'lxml')      # lxml module(parser)가 html, body가 포함된 HTML 기본 형태로 만들어 줌
print(soup)

print('='*40)

html = '''<html><head><title>test site</title></head><body><p>test1</p><p>test2</p><p>test3</p></body></html>'''
soup = BeautifulSoup(html, 'lxml')
print(soup)
print(soup.prettify())          # prettify 함수는 코드를 개행해서 보기 좋게 출력함

print('='*40)

tag_p = soup.p                  # 찾고 싶은 태그를 변수에 저장해 출력하면 바로 확인 가능, 여러 개면 첫 번째만 반환.
print(tag_p)
print(type(soup), ' : ', type(tag_p))

print('='*40)

# title 정보 추출
tag_title = soup.title
print(tag_title)
print(tag_title.text)    # text 속성을 붙이면 태그를 제외하고 내용만 반환함
print(tag_title.string)  # string 속성도 내용 반환
print(tag_title.name)    # <tag>의 이름을 반환함

print('='*40)

html = '''<html><head><title class="t" id="ti">test site</title></head><body><p>test1</p><p>test2</p><p>test3</p></body></html>'''
soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

# 태그에 있는 속성을 추출 ( 중복되는 태그가 있을 경우, 태그 별로 속성을 부여하고 속성을 찾아 추출할 수 있음 )
print(tag_title.attrs)      # attrs : 해당 요소의 속성을 추출 - 딕셔너리로 반환, 추출된 값을 확인했으니 그것에 맞춰 인덱싱하면 색인 가능
print(tag_title['class'])
print(tag_title['id'])
# print(tag_title['wow'])       # 없는 요소(없는 key)를 찾으려고 하면 에러 발생

# get()으로 속성 추출하는 것을 권장
print(tag_title.get('class'))    # 바로 인덱싱을 할 수도 있지만,
# print(tag_title.get('wow'))      get()을 사용하면 존재하지 않는 속성에 대해서 오류를 발생하지 않고 None 값을 반환
print(tag_title.get('wow', 'alternative'))
print(soup.prettify())

html = '''
<html>
 <head>
  <title class="t" id="ti">
   test site
  </title>
 </head>
 <body>
  <p>
   test0<span>
   test1</span>
  </p>
  <p>
   test2
  </p>
  <p>
   test3
  </p>
 </body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
tag_p = soup.p
p_text = tag_p.text
p_str = tag_p.string

print('text : ', p_text)
print('string : ', p_str)

"""
text는 하위 태그에 있는 문자열도 모두 추출해 줌
string은 선택한 태그의 문자열만 추출해 줌. 
==> 정확하게 추출하고 싶다면 가장 자식 요소를 선택해줘야 한다.
"""

print('='*40)

html = '''<html><head><title class="t" id="ti">test site</title></head><body><p><span>test1</span><span>test1_2</span></p><p>test2</p><p>test3</p></body></html>'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())

tag_span = soup.span
span_parent = tag_span.parent
print(span_parent)     # parent 호출 시 기준이 되는 자식도 포함되어 있음에 유의

span_parents = tag_span.parents
# print(span_parents)
for i in span_parents:
    print(i)

print('='*40)

# 형제 인식
tag_span = soup.span
next_time = tag_span.next_sibling
print(next_time)

back_time = next_time.previous_sibling
print(back_time)