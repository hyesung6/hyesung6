# 컨테이너형 - 리스트형
# 다른 변수를 담을 수 있는 변수
# keyword : []

a = []
b = [1, 2, 3]
c = ['wow', 'python']
d = [1, 2, 'wow']
e = [1, 2, ['wow', 'python']]

print(a, b, c, d, e)

# 리스트는
# a처럼 아무것도 포함하지 않아 비어 있는 리스트([])일 수 있고
# b처럼 숫자를 요솟값으로 가질 수도 있고
# c처럼 문자열을 요솟값으로 가질 수도 있다
# d처럼 숫자와 문자열을 함게 요솟값으로 가질 수도 있으며
# e처럼 리스트 자체를 요솟값으로 가질 수도
# 즉 리스트 안에는 어떠한 자료형도 포함시킬 수 있다.

print('='*40)

# 리스트 인덱싱이 가능하다. 인덱스 번호는 0번으로 시작이 동일함.
print(e[2])
print(d[-1])

# 리스트 슬라이싱
f = [1, 2, 3, 4, 5, 6, 7]
print(f[0:2])

print('='*40)

# 리스트끼리 연산
print(b[0] + b[2])

# 리스트 반복
print(b * 3)
print(d[2] + ' hi')      # 문자열을 연결시킬 경우 문자열 요소만 연결이 가능
# print(str(b[1])) + 'hi'  # 자료형이 다른 요소끼리 연산을 하면 에러 발생

print('='*40)

# 리스트 수정(변경), 삭제
a = [10, 20, 30]    # ==> [10, 15, 30] 으로 변경하고 싶을 경우
a[1] = 15
print(a)

# 연속된 범위의 값 수정
a[1:2] = ['wow', 'fantastic', 'python']
print(a)
# >> [10, 'wow', 'fantastic', 'python', 30]


# *** 연속된 범위값 수정하는 것과 인덱스를 수정하는 것은 전혀 다름
a[1] = ['wow', 'fantastic', 'python']
print(a)
# >> [10, ['wow', 'fantastic', 'python'], 'fantastic', 'python', 30]
# 상황에 맞게 수정하는 방식을 골라서 해야한다. 수정 시에도 모든 자료형을 입력받기 때문에 잘못 수정될 수 있음.

print('='*40)

# 리스트 요소 삭제
g = [10, 20, 30]

"""
g = []           # 빈 리스트를 넣어 삭제
g[1] = []        # 인덱싱 번호에 빈 리스트를 넣어 삭제
g[1:2] = []      # 슬라이싱으로 빈 리스트를 넣어 삭제

g.pop(1)         # 함수를 사용하여 삭제
del g[1]         # 함수를 사용하여 삭제
"""
print(g)

# 리스트 요소 추가하기

a.append(40)
print(a)

# append를 통해 어떠한 자료형도 추가 가능
a.append([50, 60])
a.append("hihi")
print(a)

# 리스트 정렬 : sort
b = [9, 4, 2, 10, 7]
b.sort()
print(b)

# 문자는 알파벳 순서로 정렬
str1 = ['wow', 'fantastic', 'python']
str1.sort()
print(str1)

# 리스트 역정렬 : reverse
b.reverse()
print(b)

str1.reverse()
print(str1)

# 문자열 역정렬은 오름차순이 아니라 단순 순서만 뒤집음
str1 = ['world', 'hello', 'python']
str1.reverse()
print(str1)

print('='*40)

# 위치 반환 : index
c = [10, 20, 30, 40, 50]
print(c.index(40))
# 리스트에 찾는 값이 있으면 위치값을 반환, 없으면 Error

# 리스트에 요소 삽입
# insert(x, y) : x위치에 y값을 삽입
c.insert(3, 4)
print(c)

# 리스트 요소 제거 : remove
c.remove(4)      # 제거할 때 해당 값을 찾아서 지움에 유의
print(c)

c.insert(3, 40)
print(c)

c.remove(40)     # 중복되는 값이 있으면 첫 번째 요소만 삭제
print(c)

# 리스트 요소 꺼내기 : pop
d = [1, 2, 3]
d.pop()          # 번호를 지정하지 않으면 가장 마지막 요소를 삭제
print(d)

e = [1, 2, 3, 4, 5]
e.pop(3)         # 값이 아니라 입력된 번호의 요소를 삭제
print(e)

print('='*40)

# 리스트에 포함된 요소의 갯수 세기 : count
f = [10, 20, 30, 20, 20]
print(f.count(20))

# 리스트에 있는 요소의 전체 개수 : len
print(len(f))

# 리스트 확장 : extend
g = [1, 2, 3]
g.extend([4, 5])
g.extend([6, 7])
print(g)

g += [8, 9]        # 연산자를 사용해도 같은 결과를 낼 수 있음
print(g)


print('='*100)

# for문 기본 형식

# for pattern in patterns:
#     print(pattern)

# for in : in 뒤에 쓰인 리스트 크기에 관계 없이 항상 모든 리스트에 대한 코드를 실행할 수 있음

scissors = ['가위', '바위', '보', '보', '가위', '바위', '보']

for scissor in scissors:
    print(scissor)

print('='*40)

# 1, 2, 3, 4, 5를 출력
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)

# 1부터 100까지 출력
for i in range(1, 101):
    print(i)

# for in list 형식 : 이미 내가 사용할 값이 정해져 있고, 그 목록에서 값을 꺼내 써야할 때 유용
# for in range 형식 : 횟수가 정해져 있거나, 1씩 증가하는 숫자를 쓸 때 유용

print('='*40)

names = ['봄', '여름', '가을', '겨울']
# 각 계절에 요소번호를 붙여서 출력
for i in range(len(names)):
    name = names[i]
    print('{} 요소번호 : {}'.format(i, name))

# {x}***{y}.format(x, y) 형식으로 format 함수 사용
# names 변수의 내용이 바뀌어도 수정 없이 바로 출력이 가능

names = ['봄', '여름', '가을', '겨울', '봄여름', '가을겨울']
for i in range(len(names)):
    name = names[i]
    print('{} 요소번호 : {}'.format(i, name))

print('='*40)

# enumerate() : 순서와 리스트 안의 값을 한 번에 처리할 수 있도록 해주는 함수
#             : 변수 두 개를 받는 반복문을 만들어낼 수 있어서 편리함
for i, name in enumerate(names):
    print()

print('='*40)

"""
# 함수(function)
# 코드 조각에 기능 별로 이름을 붙인 것으로, 해당 기능을 쉽게 쓸 수 있도록 도와줌
# 반복되는 부분이 있을 경우, 추후에 호출될 가능성이 있을 경우 생성하여 사용한다.
# def(define)
"""

# 기본 함수 구조
"""
def <함수명>(입력인수):
        <수행할 기능1>
        <수행할 기능2>
        ...
"""

def function1():
    print('Hello Python Function')

function1()

print('='*40)

# 입력값이 없는 함수 => 매개변수
a = 10
b = 20

def sum1():
    result = a + b
    print(result)
sum1()

# 입력값이 있는 함수 => 매개변수가 있는 함수
def sum2(x, y):
    result = x + y
    print(result)

sum2(50, 60)

print('='*40)

# 함수 구조 2 - 결과값(반환값)이 있는 함수
"""
def 함수명(입력인수):
    <수행할 문장1>
    <수행할 문장2>
    ...
    return 결과값
"""

# 결과값이 있는 함수 - 매개변수가 없는 함수
def hello():
    str2 = 'hi python function'
    return str2

print(hello())

# 결과값을 받을 변수 = 함수명()
# 변수에 함수가 반환하는 값을 저장하여 과정을 단축할 수 있음
hello = hello()
print(hello)

# 결과값이 있는 함수 - 매개변수가 있는 함수
def add(x, y):
    return x + y
add = add(100, 200)
print(add)

print('='*40)

# 실습 : 70000000만원 연봉을 받는 사원의 연봉을 10% 인상한 값을 되돌려주는 함수를 만들어보시오
# upsal(70000000) => 10% 인상된 값으로 출력되면 됨

def upsal(x):
    return x + int(x/10)
upsal = upsal(70000000)
print(upsal)

print('='*40)

def return_a():
    for i in range(100):
        return i             # return 구문은 오직 한 개의 값만 반환

print(return_a())

# return을 이용해서 어떤 상황이 되면 함수를 빠져나가도록 할 때도 자주 쓰임

def avoid(num):
    if num == 5:
        return
    print(num)

avoid(10)
avoid(5)

print('='*40)

# 함수 구조 3 - 함수 입력인수(매개변수)가 몇 개인지 모를 경우에도 사용할 수 있는 함수 만들기
"""
def 함수명(*입력인수명):        # '*'는 어떤 형식이라도 받아들이겠다는 키워드
    <수행할 문장1>
    <수행할 문장2>
    <return 결과값>           # 필요한 경우 return 사용
"""

def sum3(*args):             # args(arguments) : 관례적
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

print('='*40)

# 내장함수 : import 키워드를 사용하지 않고 즉시 사용 가능한 함수들
#           주의 - 내장함수명을 변수나 사용자정의함수의 이름으로 사용하지 말 것

import math

# 둘레 구하기
r = 10
print(r * 2 * math.pi)

# 올림 : ceil
print(math.ceil(2.4))

# 내림 : floor
print(math.floor(3.14))

# 반올림 : round
print(round(3.14))         # 반올림(round)는 내장함수 == 자주 쓰임

import random              # 0 ~ 1 사이의 무작위 실수값
print(random.random())

import webbrowser          # 기본 웹브라우저가 자동으로 실행되게 하는 모듈
webbrowser.open("http://www.example.com")

