# 1.score 리스트에 국어 , 영어 , 수학 점수가 들어있다.
# 총점과 평균을 계산해서 배열에 담은 후 모든
# 학생의 국어, 영어, 수학, 총점, 평균을 출력하시오
# 참고) 리스트에는 국어, 영어 수학 점수만 들어있다.

score = [
     [80,80,80,0,0],
     [60,50,80,0,0],
     [50,90,90,0,0],
     [40,50,60,0,0],
     [90,90,95,0,0],
     [85,95,100,0,0],
]

for i in range(0, 6):
    for j in range(0, 3):
        score[i][3] += score[i][j]
        score[i][4] = score[i][3]/3

for i in range(0, 6):
    for j in range(0, 5):
        print(round(score[i][j]), end=" ")
    print()


# 2~3 .  아래의 데이터를 정렬시키는 코드를 작성하시오. (두 가지 이상의 정렬 알고리즘을 사용 하세요 )
# # 위키피디아 검색해서 공부해오시면 됩니다. ^^
# # 리스트 내장함수를 쓰시는게 아닙니다. ^^
#  - 선택 정렬
#  - 나머지 하나
#
    data  = [100,20,5,2,3,34,65,23,66,200]

# [선택정렬 - 1]
length = len(data)
for i in range(length - 1):
    indexMin = i
    for j in range(i + 1, length):
        if data[indexMin] > data[j]:
            indexMin = j
    data[i], data[indexMin] = data[indexMin], data[i]

    print(data[i], end=' ')

# [선택정렬 - 2]

length = len(data)

indexMin = 0
temp = 0

for i in range(length - 1):
    indexMin = i
    for j in range(j + 1, length):
        if (data[j] < data[indexMin]):
            indexMin = j

    temp = data[indexMin];
    data[indexMin] = data[i];
    data[i] = temp;
    print(data[i], end=' ')

