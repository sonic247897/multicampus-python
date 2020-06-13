from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'secondapp/index.html')

# request: 사용자 요청정보가 담겨있음
def static_example(request):
    # 그냥 html파일이 아니라 렌더링 과정을 거쳐야 한다.
    return render(request, 'secondapp/static_example.html')
