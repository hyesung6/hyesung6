# 수치형(숫자형)

# 숫자는 사칙연산 가능

plus = 1 + 2
minus = 2 - 2
multiple = 3 * 3
divide = 30/5         #나누기 연산 결과값이 실수로 출력되는 이유는 나머지까지 연산을 해놓고 있기 때문
square = 2 ** 10

print(plus, minus, multiple, divide, square)

divide1 = 30/5
divide2 = 30//5        # 나눗셈의 몫 구하기 : //
remainder = 30 % 5

print(divide1, divide2, remainder)

print('--------------------------------------------')

print(0.1 + 0.1 == 0.2)         # ==가 equal을 의미하는 연산자
print(0.1 + 0.1 + 0.1 == 0.3)      # False가 출력됨.

# 일반적으로 수학에서는 실수를 정수를 포함하는 개념으로 정의
# 파이선에서의 실수는 정수와 부동소수점이라는 개념을 포함하는 것으로 정의

# 정수는 정수 영역만 다룰 수 있는 대신 항상 정확.
# 부동소수점은 실수 영역까지 다룰 수 있는 대신 완벽한 정확성을 보장하지 않음
# 부동소수점을 사용하는 이유 : 10/3 같은 연산은 3.333333이 무한히 나눠지는데, 메모리가 무한하지 않으므로
# 결국 연산을 마쳐야 하기 떄문에 실수에 대해서 근삿값을 제공하게 되어있음 ==> 완벽히 정확할 수 없다.

0.1000000000000000000000000001
0.100000000000000000000000000001
0.1000000000000000000000001

# 파이선에서는 숫자를 사용할 때 다음과 같이 경우를 나눠 사용
# 1) 정확해야 하고 정수만 써도 괜찮은 경우
# 2) 정확하지 도 않아도 되고 실수가 필요한 경우

# 필요에 따라 정수, 실수를 바꿔가며 사용할 수 있어야 함.
print(int(5.0))
print(float(5))

print(5*1.0)

print(-7/4, -7//4)
# 음수에서 // 연산자 사용 시 주의
# 나눗셈의 결과에서 무조건 소수점을 버리는 것이 아니라 나눗셈의 결과보다 작은 정수 중, 가장 큰 정수를 리턴하는 형태로 설계

print('--------------------------------------------')
# 8진수 (Octal) : 숫자가 0o 또는 0O로 시작함
octal = 0o10
print(octal)


# 16진수 (Hexadecimal) : 숫자가 0x로 시작함
hexa = 0x120
print(hexa)

print('--------------------------------------------')

name = 'Python'
age = 1991

print(name, '은', age, '년 생입니다.')

this_year = 2021 - age

print(name, '은', this_year, ' 살 입니다.')


print('============================================')


# 문자형(열) : 문자, 단어 등으로 구성된 문자들의 집합

# 문자열 만드는 방법
# 1. 큰 따옴표로 둘러싸기
string1 = "Hello Python"

# 2. 작은 따옴표로 둘러싸기
string2 = 'Hi Python'

# 3. 큰 따옴표 3개로 둘러싸기
string3 = """Funny Python"""

# 4, 작은 따옴표 3개로 둘러싸기
string4 = '''Exciting Python'''

print(string1, string2, string3, string4)

print('Jack\'s favorite food is burger.')
# 이스케이프 코드 : 미리 정의해 둔 문자 조합
# \n : 줄바꿈
# \t : Tab
# \\ : \ 출력
# \b : 백스페이스

print("===========================================")
# ctrl + /    : 주석

# 문자열 연산 : 개발자 생각을 그대로 반영해주는 파이썬의 장점

head = 'Python'
body = 'Wow'
tail = 'Fantastic'

print(head + ' ' + body + ' ' + tail)
# 여기서 '+'는 연결 연산자로 기능함

# 문자열 반복

name = '홍길동'
print(name*2)


print('='*40)
print('이것이 파이선')
print('='*40)


str01 = '재능이 있거든 가능한 모든 방법으로 사용하라. 쌓아두지 마라. 구두쇠처럼 아껴 쓰지 마라. 파산하려는 백만장자처럼 아낌없이 써라.'
# 문자열 자료형은 자동적으로 숫자를 부여함, 0부터 시작
print(str01[26])   # 인덱싱
print(str01[:20])  # 슬라이싱

# 단어 '있거든' 출력
print(str01[4:7])       # 슬라이싱의 후항의 앞 번호까지 가져온다는 뜻  == 4~6번까지 가져오려면 [4:7]

print(str01[27:])
print(str01[:-1])


regdate = '20210818WED'

# year, date, day로 구분해서 출력?

print(regdate[:4], regdate[4:8], regdate[8:])

print('='*40)

# 문자열 내장 함수 : 문자열 자료형이 자체적으로 가진 함수
# 사용 방법 : 변수 이름 뒤에 dot(.)을 붙인 다음 적절한 함수를 호출

str02 = 'apple'
print(str02.count('p'))          #'p'가 몇 개 있는지 세주는 내장 함수

str03 = '오늘은 수요일, 내일은 목요일'
print(str03.find('내일은'))       #찾는 문자가 시작하는 위치(인덱스 번호)를 반환함
print(str03.find('금요일'))       #찾는 문자가 존재하지 않으면 '-1'을 반환함
print(str03.index('내일은'))      #find와 마찬가지로 시작하는 위치의 인덱스 번호를 반환

print('='*40)

# 문자열 삽입 : Join
str10 = ','
str20 = 'abcdefg'

print(str10.join(str20))   # 문자열의 각각의 글자 사이에 지정된 값을 각각 삽입

print('='*40)

# 대소문자 변환
# 대문자로 바꾸기 : Upper
# 소문자로 바꾸기 : Lower
str11 = 'hello python'
print(str11.upper())

str12 = 'HELLO PYTHON'
print(str12.lower())

print('='*40)

# 왼쪽 공백 지우기 : lstrip
# 오른쪽 공백 지우기 : rstrip
# 양쪽 공백 지우기 : strip

# 문자열 바꾸기 : repleace
str = 'today is wed'
print(str.replace('wed', 'sat'))

# 문자열 나누기 : split
str = '오늘은 수요일, 내일은 목요일'
print(str.split())                        #구분자(입력항목)가 없으면 공백을 기준으로 문자열을 나누어줌
print(str.split(','))
print(str.split(', '))                    #인덱스번호 7~8번에 해당하는 ', '을 기준으로 문자열을 나눔
