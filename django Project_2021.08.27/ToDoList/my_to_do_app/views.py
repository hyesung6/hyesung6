from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse('장고프레임워크를 통해 처음 만들어본 페이지')
    # 데이터베이스에 저장되어 있던 할 일 목록을 모두 찾기
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index1.html', content)

def createTodo(request):
    # 1) 사용자로부터 내용을 입력받아서 넘겨 받기
    user_input_value = request.POST['todoContent']
    # 2) 넘겨 받은 내용을 데이터베이스에 입력 ==> models.py의 class Todo에 전달
    content = Todo(contents=user_input_value)
    content.save()
    # 3) 데이터베이스에 입력이 다 된 후, 처음 페이지로 이동
    return HttpResponseRedirect(reverse('index'))    # 자동으로 응답하게 하는 함수 ==> HttpResponseRedirect와 reverse 함께 사용, 각각 import해야함
    # return HttpResponse('User_ToDo_List : ' + user_input_value)

def deleteTodo(request):
    delete_Todo_id = request.GET['todoNum']
    # print('todoNum : ', delete_Todo_id)
    todo = Todo.objects.get(id=delete_Todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def completeTodo(request):
    complete_Todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=complete_Todo_id)
    todo.doDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
