from django.db import models

# Create your models here.


# 장고db가 sqlite라는 문법으로 구동하기 때문에 파이썬 문법이 아닌 sqlite에 맞는 문법으로 작성되어야 함

# 서로 같은 특성을 가진 객체들의 집합 => [동물 > 개, 고양이, 새]    이때 동물은 개, 고양이, 새의 추상화
#                                                               개, 고양이, 새는 동물의 구체화
# 공통된 특성을 하위 객체들이 사용할 수 있게 하는 것 => 상속

# models.py는 어떤 자료형으로 받아들일지 정의하는 파일

class Todo(models.Model):
    contents = models.CharField(max_length=255)
    doDone = models.BooleanField(default=False)
