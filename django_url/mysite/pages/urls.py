# pages/urls.py
from django.urls import path
from . import views # 동일한 폴더에 있는 views.py파일 가져옴
app_name = "pages"

# 변수는 꼭 urlpatterns여야 한다
urlpatterns = [
    # url을 어플리케이션마다 바꿔주면 form태그의 action url도 바꿔야 하는데
    # 하나하나 바꾸기 어려우므로 name속성을 주면 name속성대로 사용할 수 있다.
    path('index/', views.index, name="index"),
    path('menu/<str:my_name>/', views.menu, name="menu"),
    path('numbers/<int:num1>/<int:num2>/', views.numbers, name="numbers"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('throwLotto/', views.throwLotto, name="throwLotto"),
    path('catchLotto/', views.catchLotto, name="catchLotto"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
]