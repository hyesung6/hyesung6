'''
정규(표현식) - Regular Expression
특정 패턴과 일치하는 문자열을 검색, 치환, 제거하는 기능을 수행
파이썬에 기본적으로 들어가있는 모듈 ==== >   re
'''

import re

# 기본 패턴
str = """I am Hong Gil-Dong. I live in Pyeongyang.
I lived in Pyeongyang for 20 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42"""

# str에 들어가있는 자료는 문자열이지만 그 안에 숫자나 기호도 들어가있는데, 이러한 걸 구별할 수 있게끔 인식시킬 때 사용

pattern = re.compile('[a-z]')
print(pattern.findall(str))      # ==> 소문자 알파벳만 찾아줌

pattern = re.compile(('[A-Z]'))  # ==> 대문자 찾아줌
print(pattern.findall(str))

pattern = re.compile('[a-zA-Z]')  # ==> 알파벳 대소문자 찾아줌
print(pattern.findall(str))

pattern = re.compile('[a-z]+')    # ==> 해당 패턴이 연속되는 걸 찾아줌
print(pattern.findall(str))

pattern = re.compile('[0-9]')     # ==> 10진법 기준으로 숫자를 찾아줌
print(pattern.findall(str))

mp = 'My PhoneNumber is 010-1111-2222'
# 전화번호만 추출
pattern = re.compile('[0-9]+')
print(pattern.findall(mp))

print('='*40)

pattern = re.compile('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
pattern = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
pattern = re.compile('\d{3}-\d{4}-\d{4}')
