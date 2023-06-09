import random 
### 함수 정의 및 개념 ###
# -어떤 입력을 주면 output이 항상 일정해야 한다. 함수의 중요: input을 넣을 수 있어야 하고 output이 있어야 한다.
# 12일~ 함수에 대해서 더 자세히 알아봄.
# 1)내장함수 (공식문서 기준으로.) https://docs.python.org 
# A부터 Z까지 있음.
num_list = [1, 2, 3, 4, 5]

random_number = random.choice(num_list)
print(random_number) # 값을 알아보려면, python func.py로 치기.

#####
# pip install requests
import requests #requests: 밖에서 사온 함수를 의미. google에서 복사해서 고대로 밑에 입력해서 설치



URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1070'
res = requests.get(URL)
data = res.json()
drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4'] 
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]
lucky_number = random.sample(  range(1, 46) , 6 )

result = set(lotto_number) & set(lucky_number)

print(result)

