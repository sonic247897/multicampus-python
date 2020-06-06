basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruit_count = 0
nonFruit_count = 0
# 어차피 key, value 다 필요하므로 따로따로 부르지 말고 한번에 부르는 메소드를 사용하자!
# items()
for key, val in basket_items.items() :
    # 파이썬은 2중 for문을 간편화 해준다.
    if key in fruits: 
        fruit_count += val
    else:
        nonFruit_count += val
        
print(f'과일개수: {fruit_count}, 과일 아닌 개수: {nonFruit_count}')