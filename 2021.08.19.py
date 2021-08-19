# 실습 - 아이디만 추출하기

email = 'ITSA_iCORE@gamil.com'

print(email[:10])

at = email.find('@')

print(email[:at])



# 문자열 포맷 : 같은 문자열에서 특정한 값을 바꾸고자 할 때

# ex ) "오늘은 목요일입니다." -> "오늘은 금요일입니다."

# 문자열 포맷 기법 - keyword : %
# 코드 설명
# %s 문자열(string)
# %c 문자 1개(character)
# %d 정수(integer)
# %f 부동소수(floating-point)
# %% Literal % (문자 % 자체)

print('='*40)

# 1) 숫자 또는 문자열 바로 대입
print('현재 기온은 29도입니다.')
print('현재 기온은 %d도입니다.' % 28)
print('현재 기온은 %s도입니다.' % '이십칠')

# 2) 변수로 대입
cel = 26
str = '현재 기온은 %d도입니다.'
print(str % cel)

# 3) 한 개 이상의 값 formatting 가능
str2 = '오늘 기온은 %d도 입니다. %s 준비하세요'
print(str2 % (10, '우산'))

print('='*40)

# 포맷코드를 숫자와 함께 사용하기
# 1) 공백
print('%15s' % 'hi') # 전체 문자열 길이가 15인 공간에서 왼쪽부터 공백을 두고 hi를 정렬하라
print('%-15s' % 'hi')

# 2) 소수점 사용하기
print('%0.5f' % 3.142517)   # 소수점 원하는 자리까지 표현함(반올림)


# 제어문
# 조건문(분기문)
#   - if   :  수행할 문장 1
#             수행할 문장 2

people = -1

if people:
    print('사람이 한 명 있습니다.')

# 조건문 판단의 기준은 참이나 거짓이냐임. people이 1(참)을 반환하므로 조건문을 수행한다. 수치가 0만 아니면 수행함.
# 들여쓰기가 중요하다. : 코드 블럭(제어문이 구현되는 범위)을 구분해주는 역할
# 블록 - 클론(:) 다음에 들여쓴 코드 블록
#       같은 실행 흐름에서 순서대로 실행되는 코드 덩어리
#       여러 줄로 작성이 가능. 단 여러 줄일 경우 들여쓰기 칸 수가 모두 같아야함!

print('='*40)
# 조건 참/거짓을 구분할 때는 연산자 (비교, 논리) 사용
# 비교 연산자 : >, <, >=, <=, ==, !=
x = 3
y = 2

if x != y:
    print('x는 y와 같지 않다.')

# 논리 연산자 : True, False

if True:
    print('코드 블록')
    print('같은 블록')
    print('여러 줄 가능')

# 코드 블럭을 끝내려면 들여쓰기를 끝내면 됨

print('='*40)

if True:
    print('첫 번째 블록 코드')
    if False:
        print('실행되지 않을 코드')
    if True:
        print('첫 번째 - 안쪽 블록 코드')
    print('첫 번째 블록 끝 코드')
print('바깥 코드')

print('='*40)

# if <조건>:
#     <코드 블록>
# else:
#     <코드 블록>
#
# 조건이 참이면 if 코드 블록을 실행
# 조건이 거짓이면 else 코드 블록을 실행

num1 = 50
num2 = 100

if num1 > num2:
    big = num1
    print(big)
else:
    big = num2
    print(big)

print('='*40)

# 실습 - 두 값 사이의 절대값 구하기

num1 = 100
num2 = 100


if num1 > num2:
    print(num1 - num2)
else:
    print(num2 - num1)

print('='*40)

# 입력을 받는 내장함수 : input()
# value = input('숫자를 입력하세요 : ')
# print(value)

# input()은 입력되는 모든 데이터를 문자열로 취급한다.
# 조건문에서 input()으로 입력된 데이터를 사용하려면 숫자형으로 바꿔야함
score = input('숫자를 입력하세요 : ')
print(score)
value = int(score)

# 조건(분기문)
if value >= 90:
    print('당신의 학점은 "A"입니다.')
elif value >= 80:
    print('당신의 학점은 "B"입니다.')
elif value <= 79:
    print('당신의 학점은 "F"입니다.')

print('='*40)

# 제어문
# 반복문 - for문

# for 변수 in range():
#       수행할 문장 1
#       수행할 문장 2
#       ..

# range() : 숫자 리스트를 자동으로 만들어주는 함수
list1 = range(5, 10)
print(list1)  # 시작 숫자를 지정하지 않으면 0부터 입력항목 미만의 정수를 자동으로 생성
              # 콤마를 사용하여 시작, 끝 숫자 지정 가능

for i in range(1, 11):
    print('for 반복문 : ', i)

print('='*40)

# 구구단 3단 출력
for i in range(1, 10):
    print('3 * ', i, ' = ', (3*i))

print('='*40)

# 실습 : 사용자로부터 숫자를 하나 입력받아 해당 구구단을 출력해보세요

empty = input('구구단을 확인할 숫자를 입력하세요 : ')
empty2 = int(empty)
for five in range(1, 10):
    print(empty2, ' * ', five, ' = ', (empty2*five))

print('='*40)

# 1부터 10까지 한 줄에 출력
for i in range(1, 11):
    print(i, end=" ")       # end : 입력인수, end를 사용하면 다음 출력될 내용이 이어져서 나오므로
print()                     # 바로 다음 라인에 공백을 출력해서 멈춘다.

print('='*40)

# 1부터 16까지 짝수만 출력
for i in range(0, 17, 2):
    print(i)

# range()함수는 3번째 입력항목으로 step을 입력할 수 있다. ==> 2글자에 하나씩 저장


# 다중반복문 (중첩)
for dan in range(2, 10):
    for i in range(1, 10):
        print(dan, ' * ', i, ' = ', (dan*i))

print('='*40)

# 제어문
# 반복문 - while 문

# while <조건문> :
#     <수행할 문장 1>
#     <수행할 문장 2>
#     ..

# while 문은 조건문이 참이면 while문 코드 블록을 반복 실행한다.
# 무한 루프에 빠지지 않게 하려면 참인 조건을 끝나게 해야한다.

print('='*40)

# 구구단 9단 출력
i = 1
while i <= 9:
    print('9 * ', i, ' = ', (9*i))
    i += 1

# while문은 for문보다 조건을 더 정확하게 써야함. 그러므로 코드가 더 복잡
# 상황에 맞는 반복문을 선택하여 사용한다.

print('='*40)

# 실습 - while문도 중첩이 된다. 구구단 2단부터 9단까지 출력

i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print(i, ' * ', j, ' = ', (i*j))
        j += 1
    i += 1
