import requests
from pprint import pprint
# json -> dictionary
url = 'https://api.bithumb.com/public/ticker/btc'

data = requests.get(url).json()['data']
pprint(data)

# json은 문자열이므로 형변환
fluctuation = int(data['max_price']) - int(data['min_price'])
if int(data['opening_price']) + fluctuation >= int(data['max_price']) :
    print('상승장')
else :
    print('하락장')
