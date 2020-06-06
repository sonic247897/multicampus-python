# boards.py
import requests
from pprint import pprint
url = 'https://jsonplaceholder.typicode.com/posts'
# 아래에 코드를 작성하시오.
response = requests.get(url).json()

# 대괄호로 시작하는 json = list
for data in response :
    if data['userId'] == 4 :
        print(data['title'])