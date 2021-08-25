# Scrap

# requests 모듈 설치 선행
import json
import requests as rq

url = 'https://www.naver.com'

# print(rq.get(url))
# print(rq.post(url))

res = rq.get(url)
print(res)
print(res.status_code)

url = 'https://www.naver.com/a'
print(rq.get(url))      # ==> 404 오류   : 주소가 잘못된 경우 발생하는 오류
                        # ==> 405 오류   : get으로 보내면 get으로 받고, post로 보내면 post로 받아야하는데, 이 형식이 지켜지지 않을 경우 발생하는 오류

url = 'https://ko.wikipedia.org/wiki/파이썬'
res = rq.get(url)
print(res)
print(res.status_code)
print(res.headers)

# 전체 헤더스 정보를 가져오고 싶으면? ==> 딕셔너리를 사용해 반복문 작업 하면 됨
header = res.headers
for i in header:
    print(header[i])

print('='*40)

# 특정 headers 정보 추출
header = res.headers
print(header['Set-Cookie'])         # Cookie : 웹 브라우저에 저장해 놓을 수 있는 작은 정보 조각

# Cookies 속성
cookies = res.cookies
print(type(cookies))
print()
print(cookies)
print(list(cookies))

# text : HTML 코드 전부를 문자열로 반환
# text 속성은 한글 encoding issue가 생길 수 있음
url = 'https://ko.wikipedia.org/wiki/파이썬'
res = rq.get(url)
print(res)
print(res.text)

print('='*40)

# content 속성 : 한글을 binary 형태도 반환
#             : 코드화 시켜서 반환
#             : 이 속성으로 작업하는 것을 더 권장
print(res.content)

print('='*40)

# 인코딩 확인
print(res.encoding)

# 웹 페이지 이동 --> 링크를 클릭해서 이동하는 행위는 결론적으로 주소를 바꾸는 것
# --> 내가 표시할 페이지에서 다른 페이지의 정보를 보낼 수 있어야함

# 주소창 정보 처리
# 1) 직접 접근 가능
url = 'https://ko.wikipedia.org/wiki/파이썬?key1=value1&key2=value2'
res = rq.get(url)
print(res)
print(res.url)

# 2) parameter 속성 통한 접근 - 딕셔너리 형태 (권장)
url = 'https://ko.wikipedia.org/wiki/파이썬'
res = rq.get(url, params={'key1':'value1', 'key2':'value2'})
print(res)
print(res.url)

# 3) json을 통한 접근 (권장)
url = 'https://ko.wikipedia.org/wiki/파이썬'
res = rq.get(url)
print(res)
print(res.url)
print(json.dumps(res.url))

print('='*40)

dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {"key1": 'value1', "key2": "value2"}

print(str(dict1))
print(json.dumps(dict1))

print('='*40)

print(str(dict2))
print(json.dumps(dict2))

# 일반 문자열 str() 은 작은 따옴표, 큰 따옴표의 사용에 관계 없이 작은 따옴표로 출력된다.
# 딕셔너리 형태를 유지하면서 문자열로 바꾸는 결과 (json 사용)는 큰 따옴표로 결과값이 나온다.
# 일반 문자열로 표현하는 방식은 작은 따옴표로 나와서 오류가 발생할 수 있음
# json을 사용하는 방법을 권장

# url에 http, https을 명시하지 않으면 에러