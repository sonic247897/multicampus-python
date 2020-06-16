# Django ORM
---
## CREATE
**1. INSERT INTO TABLE이름 (column1, column2, ..) VALUES (values1, values2, ...) [sql] **

**[ORM]**

``` python
>>> from articles.models import Article

# 첫 번째 방법
article = Article()
article.title = 'first'
article.content = 'django!'
article.save() # DB에 적용(저장)

>>> article
<Article: Article object (1)> # 안의 숫자는 pk

# 두 번째 방법
# Article(id, title, content, created_at, updated_at)
# id가 생략되어 있을 뿐 자동으로 생성되므로, 어느 변수에 어떤 값을 넣을건지 명시 
article = Article(title='second', content='django!')
article.save()

>>> article
<Article: Article object (2)> # 안의 숫자는 pk
    
# 세 번째 방법
# - 저장도 자동으로 됨/ objects는 DB와 연결해준다.
Article.objects.create(title='third', content='django!')
<Article: Article object (3)>
```

---

## READ

**2. SELECT * FROM TABLE이름(articles_article) **

``` python
# 전체 조회
article = Article.objects.all()

>>> article
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
# QuerySet은 list처럼 작동한다 => index접근 가능
>>> article[0].title
'first'

>>> Article.objects.all()
<QuerySet [<Article: 1번째글 - first : django!>, <Article: 2번째글 - second : django!>, <Article: 3번째글 - third : django!>]>
```



**3. SELECT * FROM articles_article WHERE title='first'**

``` python
# 특정 제목 불러오기
# 모델이름.objects.~
Article.objects.filter(title='first')
<QuerySet [<Article: 1번째글 - first : django!>]>
```



**SELECT * FROM articles_article WHERE title='first' LIMIT 1**

``` python
# filter로 가져올 때는 한 개밖에 없어도 리스트 형태로 가져온다.
# 아무것도 없으면 빈 QuerySet을 반환
Article.objects.filter(title='first').first()
Article.objects.filter(title='first').last()
Article.objects.filter(title='first')[0]

>>> Article.objects.filter(pk=10)
<QuerySet []>
```



**SELECT * FROM articles_article WHERE id=1**

``` python
# 고유값으로 찾아오기 => 객체 형태로 가져온다.
Article.objects.get(id=1) # id는 쓰이는 곳이 많기 때문에 헷갈릴 수 있으므로 pk를 쓰기로 한다!
Article.objects.get(pk=1)
# 주의점
# 고유값이 아닌 내용을 필터링해서
# 2개 이상의 값이 찾아지면 오류가 발생한다.(리스트 형태가 아니므로)
# + 없는 것을 가지고 오려고 해도 오류 발생

>>> Article.object.get(pk=10)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Article' has no attribute 'object'
    
>>> Article.objects.get(id='first')
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```



**Like / startwith / endswith**

- 장고에서 기본으로 제공해주는 필터

``` python
# 특정 문자열을 포함하고 있는가
Article.objects.filter(title__contains='fir')
# 특정 문자열로 시작하는가
Article.objects.filter(title__startswith="se")
# 특정 문자열로 끝나는가
Article.objects.filter(title__endswith="ha")
```

**ASC / DESC**

``` python
# 기본 오름차순
Article.objects.all().order_by('pk') 
# 음수를 붙이면 내림차순
Article.objects.all().order_by('-pk') # DB단에서 내림차순으로 처리
# 게시판에서 최신글이 위로 올라오게 할 때 사용
Article.objects.all()[::-1] # 이미 가져온 QuerySet을 파이썬에서 처리(리스트 연산)
# [::]는 전체, [1:3:2]는 첫번째부터 3번째 전까지 2단계씩 slicing
```



---

## UPDATE

**UPDATE articles_article SET title='byebye' WHERE id=1 **

``` python
# 수정
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
```

---

## DELETE

**DELETE FROM articles_article WHERE id=1**

``` python
# 삭제
article = Article.objects.get(pk=1)
article.delete() # DB 상에서 삭제된 것이므로 article에는 아직 title과 content가 저장되어 있다.
# 그러나 직접 pk를 조작해서 다시 DB에 넣는 방식은 좋지 않다. => 마지막에 어떤 정보가 사라졌음을 사용자에게 보여줄 때 사용 가능 ex) OOO님 지금까지 이용해주셔서 감사합니다.
# 따로 저장하지 않아도 자동으로 저장된다.
(1, {'articles.Article': 1})
```

---

- 추가

``` python
>>> article = Article()
# pk, created_at, updated_at는 DB에 반영될 때 생성되는 것이므로 아무것도 출력되지 않는다.
>>> article.pk
>>> article.created_at
>>> article.updated_at
# 아무것도 지정해주지 않았으므로 비어있다.
>>> article.title
''

>>> article.title = 'first'
>>> article.content = 'django!'
>>> article
<Article: None번째글 - first : django!>
        # => 아직 DB에 반영되지 않아서 title과 content만 출력된다.
>>> article.save()
>>> article.created_at
datetime.datetime(2020, 6, 16, 1, 15, 57, 559736, tzinfo=<UTC>)
>>> article
<Article: 5번째글 - first : django!>
        # => 1번째 글을 지우고 insert 했지만 1번째 글이 아니라 5번째 글로 넘어간다.(auto increment)
```



