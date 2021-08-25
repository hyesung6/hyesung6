# urllib module

from urllib.request import urlopen, Request

url = 'http://example.com'

# urllib는 Request 객체를 만들어서 요청
req = Request(url)
print(req)

print('='*40)

# 객체를 통해 url 접근을 수행
page = urlopen(req)
print(page)

print('='*40)

print(page.code)
print(page.headers)
print(page.url)
print(page.info().get_content_charset())

print('='*40)

# 페이지 내용 추출
print(page.read())   # 바이너리 형태로 추출

print('='*40)

import urllib
url = 'http://example.com'
req_get = Request(url+"?key1=value1&key2=value2", None, headers={})
# Request 객체 이용시 (url, method, headers) 형태가 되어야한다.
# Request 객체 paramer에서는 두번째 인자가 있으면 post, 없으면 get
page = urlopen(req_get)

print(page)
print(page.url)

print('='*40)

# post 방식
# 요청 시 보낼 데이터는 바이너리 형태로 인코딩해서 보내야함. 받을 때 바이너리 형태이기 때문.
data = {'key1': 'value1', 'key2': 'value2'}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

req_post = Request(url, data=data, headers={})
page = urlopen(req_post)

print(page)
print(page.url)


"""
requests 와 urllib
1) url을 통한 요청 시 요청 객체를 생성하는 방법에 차이
2) 데이터 전송 시 requests는 딕셔너리, urllib는 인코딩 처리가 된 바이너리 형태
3) requests를 통한 요청 형태는 (get(), post())를 명시해야함
   urllib를 통한 요청 형태는 Request 객체 안의 인자 여부(두 번째 인자의 유무)
4) 페이지 주소의 오류가 있을 경우에는 urllib는 다 에러를 발생하고 에러코드를 띄워준다.
"""


