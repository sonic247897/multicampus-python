from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    # 파일이 있는 경로 명시(장고에서 기본적으로 templates폴더를 찾는다)
    return render(request, 'pages/index.html')

# 1. 사용자가 url 경로에 이름을 입력하면
# 2. 그 이름과 무작위 음식 하나 보여주는 템플릿 페이지 작성
# 2-1. random.choice(menu리스트)
# 3. urls -> views -> template 순으로 작성
def menu(request, my_name):
    menuList = ['삼겹살', '수육', '갈비', '보쌈', '치킨']
    menu = random.choice(menuList)
    context = {
        'my_name' : my_name,
        'menu' : menu
    }
    return render(request, 'pages/menu.html', context)

def numbers(request, num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2
    }
    return render(request, 'pages/numbers.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

# input태그에 입력한 값은 request에 담겨있다.
def catch(request):
    # query_dict : 파이썬에서 사용하는 dictionary와 유사
    name = request.GET.get('name') # GET: GET방식으로 보냈기 때문
    age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/catch.html', context)

# 1. 사용자가 숫자 입력
# 2. 입력받은 횟수만큼 반복해서 
# 3. 리스트에 로또 번호 담는다.
# 3-1. random.sample(range(1,46), 6) : 1~45번 6개(중복가능)
#       리스트에 append
# 4. 사용자가 입력한 숫자와 로또번호가 담긴 리스트를 출력[로또 n장 사기]
# 5. ul태그를 사용하여 각 번호들을 한 줄씩 출력
# 6. urls -> views -> template
def throwLotto(request):
    return render(request, 'pages/throwLotto.html')

def catchLotto(request):
    # form태그에 method속성 안 적어주면 자동으로 GET
    count = int(request.GET.get('count'))
    lottoList = []
    # 정렬 작업 등은 파이썬에서 처리!
    for i in range(count):
        lotto = sorted(random.sample(range(1, 46), 6))
        lottoList.append(lotto)
    context = {
        'count' : count,
        'lottoList': lottoList
    }
    return render(request, 'pages/catchLotto.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    message = request.GET.get('message')
    # json이 아니고 문자열이므로 .text()
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)
