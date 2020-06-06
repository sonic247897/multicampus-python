import requests
from pprint import pprint # pprint가 갖고 있는 pprint 가져와서 사용
import random

response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=913')
print(response) # <Response [200]>
# JSON - dictionary 형식이므로 dictionary로 형변환 해주는 함수 사용
data = response.json()
pprint(data) # pprint - pretty 예쁘게 출력

winner = []
for num in range(1,7) :
    #winner.append(data['drwtNo'+str(num)]) # 문자열+정수 불가능
    winner.append(data[f'drwtNo{num}']) # fstring(보간법) 이용 - 형변환 없어도 문자열로 작동
print(winner)

 # 2. 내가 당첨된 등수 딕셔너리에 저장하기
win_rate = {
        '1st' : 0,
        '2nd' : 0,
        '3rd' : 0,
        '4th' : 0,
        'fail': 0
    }
# 1. 천 번 반복하기
ranking = []
for i in range(1000) :

    my_lotto  = random.sample(range(1,46), 6)

    matched =0
    for num in my_lotto:
        #print(num)
        if num in winner :
            matched += 1
    
    if matched == 6 :
        win_rate['1st'] += 1
    elif matched == 5 :
        if data['bnusNo'] in my_lotto :
            win_rate['2nd'] += 1
        else :
            win_rate['3rd'] += 1
    elif matched == 4 :
        win_rate['4th'] += 1
    else : 
       win_rate['fail'] += 1

# 3. 해당 딕셔너리 최종적으로 한 번만 출력하기
print(win_rate)