# 1. 태어난 년도 4자리 입력받아서 화면에 당신의 띠 출력해보기

# 자축인묘   진사오미     신유술해
# 쥐소호토   용뱀말양     원닭개돼
# 4 5 6 7   8 9 10 11  0 1 2 3

birth = input('태어난 년도 4자리 입력 : ')
year = int(birth) % 12
if year == 0:
    print('원숭이')
if year == 1:
    print('닭')
if year == 2:
    print('개')
if year == 3:
    print('돼지')
if year == 4:
    print('쥐')
if year == 5:
    print('소')
if year == 6:
    print('호랑이')
if year == 7:
    print('토끼')
if year == 8:
    print('용')
if year == 9:
    print('뱀')
if year == 10:
    print('말')
if year == 11:
    print('양')
print()

# [다음 형태로 출력해보기] - 반복문 사용
# 2.
#      1
#      12
#      123
#      1234
#      12345
#      123456
#
for cycle in range(1, 8):
    for cycles in range(1, cycle):
        print(cycles, end=' ')
    print()
print()

# 3.
#      *
#      **
#      ***
#      ****
#      *****
#
for stars in range(0, 6):
    print("*" * stars)
print()

# 4. 몇 줄 출력?
# 3
#        *
#        **
#        ***
star1 = input('별이 몇 줄? : ')
star2 = int(star1)
for stars in range(0, star2):
    for star in range(stars+1):
        print('*', end='')
    print()
print()

# 5.
#        *****
#        ****
#        ***
#        **
#        *
#
for stars in range(5, 0, -1):
    print("*" * stars)
print()

# 6. 구구단 2단 부터 9단까지 출력하는 코드를 작성하시오
#
i = 1
while i < 9:
    i += 1
    j = 1
    print("=" * 30)
    while j <= 9:
        print(i, " * ", j, "는", (i*j), "입니다.")
        j += 1
print()

# 7. 사용자로부터 값을 입력받아 해당 단을 출력하는 코드를 작성하시오
# 몇단? 3
# 3단 출력
gugu1 = input('구구단을 확인할 숫자를 입력하세요 : ')
gugu2 = int(gugu1)
for gugu in range(1, 10):
    print(gugu2, ' * ', gugu, ' = ', (gugu2*gugu))
print()

# 8.  1부터 입력한 숫자까지의 누적합을 출력하시요
#
# 출력 결과
#
# 얼마?  100
#
#
# 1부터 100까지 합은 5050 입니다.
#
i = 1
j = 0
while i <= 100:
    j += i
    i += 1
print(1, "부터", 100, "까지 합은", j, "입니다.")
print()



# 9. 다음 결과를 출력하세요 (while 문)
# 1. 1000이하의 자연수 중에서 2의 배수이면서 7의 배수인 숫자 출력
# 2. 그 숫자들의 합

a = 1
b = 0
while a <= 1000:
    if a % 14 == 0:                  # a % 2 == 0 & a % 7 == 0
        print(a)
        b += a
    a += 1
print('b :', a)
