from django.db import models

# Create your models here.

# 파이썬 convention - 단수형태. 맨 앞글자 대문자!!
# 장고가 미리 만들어 놓은 객체를 상속받는다.
class Article(models.Model): 
    # DB에 생성되는 테이블 이름: articles_article (app이름_클래스이름)
    title = models.CharField(max_length=150) # CharField는 max_length를 반드시 넣어줘야 함
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # DB에 생성한 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정되는 시간 저장
    #boolean = models.BooleanField(blank=True) # blank=True: 비어있어도 상관없다
    
    # 매직 메소드(객체를 예쁘게 출력해주는 특수 메소드)
    #   => migrate는 할 필요 없지만 shell은 다시 켜야 한다.
    def __str__(self): # 인스턴스 메소드
        return f'{self.id}번째글 - {self.title} : {self.content}'
    