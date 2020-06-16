from django.urls import path
# views.py가 urls.py와 동일한 위치에 있음
from . import views

app_name = "articles"

urlpatterns = [
    # 이름 - 1. 또 다른 app을 생성했을 때 어디로 가야할지 참조하기 위해 지음
    #       2. 수정시 모든 페이지의 경로를 수정하지 않아도 되도록
    path('', views.index, name="index"), # articles/로만 접속할 수 있다.
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    # variable routing: view함수에서 사용
    path('<int:article_pk>/', views.detail, name="detail"),
    path('<int:article_pk>/delete', views.delete, name="delete"),
    path('<int:article_pk>/edit', views.edit, name="edit"),
    path('<int:article_pk>/update', views.update, name="update"),
]