import requests 
from bs4 import BeautifulSoup #대문자로 시작함으로서 두 단어가 합쳐졌다는 것을 알 수 있음.
URL = 'https://finance.naver.com/sise/' #변하지 않는 문자: 대문자로 작성.

res = requests.get(URL) # ; 주소를 보내주면 이에 대한 답을 해주는 것의 의미.
#항상 오른쪽을 먼저 적고 난 뒤, 왼쪽을 채워넣음. 중간중간에 데이터가 어떻게 변하는지 예측하면서 코드 만들기.
print(res)

data = BeautifulSoup(res.text, 'html.parser')
#200: 전혀 문제가 없다는 의미. 앞자리가 2로 시작하면 정확하게 뭔가가 잘 이루어졌다는 의미.
selector = '#KOSPI_now'
kospi = data.select_one(selector)

print(kospi)

################################


selector = '#KOSDAQ_now'
kosdaq = data.select_one(selector)

print(kosdaq)