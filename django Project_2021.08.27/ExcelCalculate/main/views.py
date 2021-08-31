# main views.py

from django.shortcuts import render, redirect
from .models import *
from random import *
from sendEmail.views import *

# Create your views here.
def index(request):
    return render(request, 'main/index2.html')

def signup(request):
    return render(request, 'main/signup.html')

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    content = {}
    content['grade_calculate_dic'] = request.session['grade_calculate_dic']
    content['email_domain_dic'] = request.session['email_domain_dic']

    # session 처리 다 됐으면 결과 출력하고 session에서 데이터 삭제 (권장)
    del request.session['grade_calculate_dic']
    del request.session['email_domain_dic']
    return render(request, 'main/result.html', content)
    #return render(request, 'main/result.html')

def join(request):
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']

    print(name, email, pw)

    # 인증코드 4자리 정수로 생성
    code = randint(1000, 9999)

    # 쿠키에 저장
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)

    # 인증코드 - 이메일로 전송
    send_result = send(email, code)

    if send_result:
        return response
    else :
        return HttpResponse('이메일 발송에 실패했습니다.')

def verify(request):
    user_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')

    #print(user_code, cookie_code)
    if user_code == cookie_code:
        # 이메일 인증이 된 경우
        return redirect('main_index')










