'''
컨테이너형 - 사전형(Dictionary)
기본형식
dic - {key1: value1, key2: value2, key3: value3, ....}
'''

wager = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}

print(wager)
print(wager['보'])        # 딕셔너리는 키를 통해 밸류를 찾음
a = [x for x, y in wager.items() if y == '바위']    # 밸류로 키 구하기
print(a)

print('='*40)

# 가위바위보 승패판정 함수 만들기

def rsp(x, y):     # 내가 낸 것 x , 상대 y
    if x == y:
        return "무승부"
    elif wager[x] == y:
        return "승리"
    else:
        return "패배"

result = rsp('보', '가위')
print(result)

# key는 value를 찾기 위한 값이므로 유일해야 함. 그래서 리스트를 사용할 수 없음.
# value에는 리스트를 사용할 수 있다.

print('='*40)

# 리스트 생성
list1 = [1, 2, 3, 4, 5]

# 3번 째 값 수정
list1[2] = 33

# 리스트에 새로운 값을 추가
# list1[5] = 6          # 없는 인덱스에 값을 추가하면 오류
list1.append(6)
print(list1)

print('='*40)

# 딕셔너리
dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1)

# 딕셔너리 수정           # 덮어쓰기 형식으로 수정하는 점은 비슷하지만, 인덱스가 아닌 key를 호출하여 수정
dict1['three'] = 33
print(dict1)

# 새로운 값 추가 - append() 함수가 없다. 그냥 선언하면 추가가 됨
dict1['four'] = 4
print(dict1)

# 딕셔너리 삭제           # 리스트와 같은 방식으로 삭제한다. 인덱스가 아니라 [key]를 호출하여 삭제
del(dict1['four'])
print(dict1)

# dict1.pop()           # 리스트는 그냥 pop()을 실행하면 마지막 요소가 빠져나가지만, 딕셔너리는 오류 발생함
dict1.pop('three')                                              # 딕셔너리는 데이터 순서가 없기 때문
print(dict1)

print('='*40)

seasons = ['봄', '여름', '가을', '겨울']
for i in seasons:
    print(i, end=' ')
print()

print('='*40)

result = {'Python': 90, 'Web': 90, 'Bigdata': 80}
print(result)

'''
key, value 각각 호출 가능
'''

for key in result.keys():
    print(key)

for value in result.values():
    print(value)

# 과목과 점수 모두 출력 - key를 가져오는 게 우선
for key in result.keys():             # 딕셔너리 자료형은 key로 호출되는 형식이므로 keys()함수가 생략되어도 인식됨
    print('{} 점수는 {} 이다.'.format(key, result[key]))

print('='*40)

# 리스트의 인덱스 번호를 통해서 값을 구하는 방식  --> enumerate()를 통해 두 가지 정보를 처리
# 딕셔너리도 enumerate()와 같은 기능을 하는 함수가 있다.  --> items()

for key, value in result.items():
    print('{} 점수는 {} 이다.'.format(key, value))

"""
딕셔너리 요소들은 출력 순서가 다를 수 있음
리스트와 달리 딕셔너리는 순서를 지켜서 리턴을 해주지 않기 때문 ==> Key로 찾으므로 순서를 지킬 필요가 없음
"""

print('='*40)

"""
컨테이너형 - 튜플(tuple)
순서가 있는 값의 집합이고 만들어지고나서 변경을 최소화할 때 사용함
리스트는 [] 대괄호,     딕셔너리는 {} 중괄호,   튜플은 () 소괄호
"""

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# 튜플을 만들 때 소괄호가 핵심요소는 아님. 핵심은 콤마(,)

tuple2 = 1, 2, 3, 4, 5
print(tuple2)
print(type(tuple2))

# 튜플을 리스트로부터 생성 가능
list1 = [1, 2, 3, 4, 5]
tuple3 = tuple(list1)
print(tuple3)

# 튜플 값 가져오기
print(tuple3[0])

# 튜플 값 출력
for i in tuple3:
    print(i, end=' ')
print()

print('='*40)

# 튜플 값 수정            ---> 튜플은 리스트와 같은 방식으로 값 수정이 불가능함
# tuple3[2] = 22
# print(tuple3)

# 튜플 값 삭제            ---> 삭제도 마찬가지로 안 됨
# del tuple3[2]
# print(tuple3)

"""
튜플의 값을 수정/삭제하려고 하면 TypeError가 발생함
튜플은 순서와 값을 모두 고정하고 있기 때문
그래서 수정, 삭제(del, pop) 모두 사용 불가
"""

print('='*40)

a = 1
b = 2
print(a, b)

a, b = 1, 2
print(a, b)         # 튜플이 이루어진 상태 :  a = 1, b = 2

c = (3, 4)          # 변수 c에 튜플로 3, 4를 대입  ==> 패킹
print(c)

d, e = c            # 변수 d와 e를 각각 대입      ==> 언패킹
print(d, e)

"""
패킹 : 하나의 변수에 여러 개의 값을 대입
언패킹 : 패킹된 변수에서 여러 개의 값을 꺼내오는 것
"""

# 데이터 맞바꾸기(Swap)
x = 5
y = 10
print(x, y)

temp = x             # 다른 언어에서 바꾸려면 임시파일을 이용해 저글링하듯이 바꿈
x = y
y = temp
print(x, y)

print('='*40)

x = 5
y = 10
x, y = y, x          # 튜플로 맞바꿈 -> 훨씬 편리하다. 파이썬의 장점 중 하나
print(x, y)

print('='*40)

# 여러 개의 값을 반환할 때 유용
# 하나의 함수는 하나의 값만 반환하는 것이 기본적
def tuple_return():
    return 1, 2

num1, num2 = tuple_return()
print(num1, num2)
print(type(tuple_return()))       # 튜플 클래스로 출력된다.

print('='*40)

list1 = [1, 2, 3, 4, 5]
for i, v in enumerate(list1):
    print('{}번 째 값 : {}'.format(i, v))
print()

# 리스트를 통째로 넣기만 했는데 인덱스 번호를 알아서 저장함을 알 수 있다.
# 튜플로 인식한다는 것

for j in enumerate(list1):
    print('{}번 째 값 : {}'.format(j[0], j[1]))
print()

for k in enumerate(list1):
    print('{}번 째 값 : {}'.format(*k))

print('='*40)

# 리스트 자료형이 튜플처럼 인식되어 아주 간단하게 정의할 수 있는 것처럼
# 딕셔너리에서도 가능하다. 딕셔너리의 enumerate() 기능을 하는 함수 - items()

result = {'Python': 90, 'Web': 90, 'Bigdata': 80}

for key, value in result.items():
    print('{} 과목 점수는 {} 입니다.'.format(key, value))

# 실습 - 더 줄여서 출력하기

for key in result:
    print('{} 과목 점수는 {} 입니다.'.format(key, result[key]))

# 딕셔너리 result를 통째로 넣고 key만 호출해도 value가 같이 묶여있기 때문에 간단하고 보기 쉬운 코드를 짜는 것이 가능하다
# result[key]는 딕셔너리의 value 이기 때문


