import requests
from pprint import pprint
key = 'AIzaSyA5pDkMG03qwd5p3-7oLopX2YZ4cbTqlDg'
# 1. 검색어를 입력하면
# string interpolation
search = input("검색어를 입력해 주세요: ")
# 구글의 검색 규칙: search?q=
q = f'q={search}'
# 특정 리소스 항목만 검색
my_type = 'type=video'
# 필수 매개변수 snippet: 영상에 대한 정보 들어있음, id: id 들어있음
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}'
print(url)


# # 2. 영상들을 검색할 것
# response = requests.get(url)
# #print(response) # <Response [200]>
# print(type(response.json())) # <class 'dict'> =>파이썬의 dictionary형태로 변환해 준다.
# datas = response.json()
# pprint(datas)


# # 3. 그 영상들의 제목과 채널명 출력
# # datas['items']는 list
# for data in datas['items']:
#     # dictionary 안에 dictionary
#     print(data['snippet']['title'], end=' 채널명 ') # end: print 두 개 사용하는데 한 줄 출력
#     print(data['snippet']['channelTitle'])

# resultsPerPage 늘리기, slicing으로 10개만 뽑아보기
maxResults = 'maxResults=20'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{maxResults}&{q}'
print(url)

response = requests.get(url)
datas = response.json()

# list에서 0~9번만(10개)
for data in datas['items'][:10]:
    print(data['snippet']['title'], end=' 채널명 ')
    print(data['snippet']['channelTitle'])

# => id를 연결하면 html에서 바로 영상도 연결 가능하다.