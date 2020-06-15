from django.shortcuts import render

# Create your views here.
def index(request):
    # 파일이름X. 경로!
    # articles_index.html로 해도 되지만 이름이 너무 길어지므로 
    # templates 폴더 안에 app 이름으로 폴더 하나 더 만든다.
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # request.GET은 query_dict 타입이므로 키값으로 값을 가져올 수 있다.(get메소드)
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    return render(request, 'articles/create.html', context)

# 1. /introduce/ 경로
# 2. h1 태그로 이루어진 제목
# 2-1. 각각의 p태그에 이름과 나이 작성
# 3. back 링크로 index로 돌아갈 수 있는 링크 하나
# 4. index에서 introduce로 이동할 수 있는 링크 하나
# 5. base.html 상속받아서 block body 안에 작성
def introduce(request):
    return render(request, 'articles/introduce.html')

