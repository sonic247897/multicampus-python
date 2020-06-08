# random.py
import random
# 모듈에서 사용할 수 있는 메소드 목록 출력
#print(dir(random))
pick = random.choice(range(10))
print(pick)

pick = random.choice([1,2,3,4,5])
print(pick)

# q로 빠져나오면 된다
#help(random.choice)
#help(random.sample)

# 중복된 수 없이 뽑고 싶을 때
pick = random.sample(range(10), 3)