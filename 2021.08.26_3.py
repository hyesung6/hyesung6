'''
- 모듈(라이브러리)  :  공구함
                 :  task에 맞는 도구를 사용

- 프레임워크       :  자동차
                 :  내가 직접 엔진 구동의 메커니즘을 구현할 필요없이, 자동차만을 움직이기 위해 기어 넣고 엑셀만 밟으면 됨.
                 :  프레임워크는 객체들의 제어 권한을 가져가기(제어의 역흐름) 때문에, 프레임워크가 알아먹을 수 있는 형식으로 만들어서 넣어줘야만 함
이라는 느낌으로 차이점을 이해하면 된다.
'''

'''
django  :  Full Stack Framework
Flask   :  Micro Framework
'''

'''
클라이언트는 OS>웹브라우저를 통해 서버가 가지고 있는 HTML파일에 접근(요청)
서버는 HTML 요청에 대한 응답
WAS(Web Application Server)가 서버(OS>서버프로그램)의 HTML파일을 해석해서 내보내주는 역할
was가 있어야 서로 다른 os여도 요청응답이 가능함
'''

import django
print(django.get_version())