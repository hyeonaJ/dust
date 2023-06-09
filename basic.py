# 변수, variable (변경가능함)
dust = 10
- dust라는 변수에 숫자 10을 넣어주세요.라고 해석

dust = '10' 
greeting = 'hello'

# 1
status = True
 # 0 (주석의 의미)
 # 0
status = False
# 참과 ture는 대문자로 적어야 함. &어떤 변수에 데이터를 두 번 집어넣으면 그 값이 바뀐다.


print(dust, greeting, status)
+앞으로 코드작성 시 3가지 주의점
# 1. apple, Apple (같지 않음.) 대 소문자가 다르기 때문. 
# 2. git add. / git add . 띄어쓰기가 있고 없고에 따라 완전히 다름
# 3. message / massage 가장 많이 실수하는 변수. 오타발생. 스펠링이 틀리면 에러발생
# + 대괄호[]: 여러개의 데이터를 저장.
dust_list = [10, 20, 20, 15, 100, 150]
print(dust_list[2]) ; 0 1 2 3 4 식으로 읽는다. dust_list[0]이면 10을 의미.
#dict: dictionary의 약자
dust_dict ={
    '서울': 100,
    '대전': 50,
    '부산': 10,
}
print(dust_dict['서울']); 서울만 불러올 때

 # 조건
age = 10

if age > 20:
    print('성인입니다')
elif age > 8:
    print('청소년입니다')
else:
    print('어린이입니다')

# 반복
menus = ['짜장면', '국밥' , '김밥' , '라면' , '피자']

n = 0
while n < 2:
    print(menus[n])
    n = n + 1

# for menu in menus: 여기서 부터 여기까지 반복해줘. 라는 명령어는 for
for menu in menus:
    print(menu)