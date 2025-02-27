#60강 - 튜플, 이뮤터블자료, 뮤터블 자료
#튜플 : ()로 만듬. 리스트와 비슷함.
# a=(1,2,3)
# print(a)
# print(type(a))
# print(a[0])
# print(a[1])
# #요소를 하나 갖는 튜플?
# b=(1, )
# print(b, type(b))

    # 튜플과 리스트의 차이
#리스트는 인덱스로 접근해서 내부 내용 변경 가능.
#ex) a[5] = 3 
#but, 튜플은 요소를 변경할 수 없음.

# #튜플과 함수리턴
# #(1)
# def a():
#     return (10,20,30)
# (b,c,d)= a()
# #(b,c,d) = (10,20,30)
# print(b,c,d)
# #(2)
# A= ["바나나", "사과","고구마", "감자"]
# for item in enumerate(A):#튜플로 결과 출력. (인덱스,요소)형식
#     print(item) 
# #(3)
# B={
#     "이름":"별",
#     "생일": (2019,11,14)
# }
# for key, value in B.items():
#     print(key, value)

# #요소를 변경할수 없는 특성 활용

# #자료: 뮤터블자료+이뮤터블자료
# #이뮤터블: 변수에 넣었을 때 스택에 있는 값을 변경해야만 +값을 변경할 수 있는 자료
# a=10
# a=20 #숫자, 불, 문자열, 튜플 이뮤터블
# c="안녕하세요"
# c[1] = "가" #>>에러. 이뮤터블이기 때문.

# #뮤터블자료: 변수에 넣었을때 스택에 있는 값을 변경하지 않아도 +값을 변경할 수 있는 자료
# #리스트, 딕셔너리
# A={
#     # [10,20] : 10 #에러 
#     (10,20) : 10 #동작
# }

#########################
#61강 -콜백함수, map/filter함수
#함수는 변수에 저장할 수 있다.
# def call_10_times():
#     print('함수호출')
# a = call_10_times
# print(a) #결과: function call_10_times at 0x7fc070e4ff40>
# a() #결과: 함수호출

# def call_10_times(콜백함수):
#     for i in range(10):
#         콜백함수(i)
    
# def print_hello(매개변수):
#     print('안녕하세요', 매개변수)

# call_10_times(print_hello) #매개변수를 함수로 전달

# #map()
#각각의 요소에 함수를 적용해서
#새로운 리스트(이터레이터)를 리턴한다.
# 이터레이터 = map(함수, 리스트)
# def power(숫자):
#     return 숫자 **2

# A=[1,2,3,4,5]
# 이터레이터 = map(power, A)
# print(list(이터레이터))
# #리스트내포로 활용
# print([
#     #표현식
#     숫자 **2
#     #반복문
#     for 숫자 in range(1,5+1)
# ])

# #filter(함수,리스트)
# # 리스트의 요소를 함수에 전달했을 때
# # 결과로 True가 나오는 녀석들만 모아서 
# # 새로운 이터레이터를 만듦
# def 홀수인가요(숫자):
#     if 숫자 %2 ==1:
#         return True
#     else:
#         return False
# A = [1,2,3,4,5]
# 이터레이터 = filter(홀수인가요, A)
# print(list(이터레이터))

# #리스트 내포로 사용(위와 같은 결과)
# print([
#     #표현식
#     숫자
#     #반복문
#     for 숫자 in range(1, 5+1)
#     if 숫자 %2 ==1
# ])
############################
# #62강 - map/filter 함수 직접 구현하기
#     #map()
# def my_map(콜백함수, 리스트):
#     output = []
#     for 요소 in 리스트:
#         output.append(콜백함수(요소))
#     return output
# def power(숫자):
#     return 숫자 **2
# A=[1,2,3,4,5]
# print(my_map(power, A))

#     #filter()
# def my_filter(콜백함수, 리스트):
#     output = []
#     for 요소 in 리스트:
#         if 콜백함수(요소) : # == True
#             output.append(요소)
#     return output
# def is_odd(숫자):
#     return 숫자%2 == 1
# print(my_filter(is_odd, A))
############################
# 63강 - 람다, key 키워드 매개변수
#람다 : 간단한 함수를 간단하게 해주는 문법

# # 일반함수
# def power(숫자):
#     return 숫자 **2
# def is_odd(숫자):
#     return 숫자 %2 ==1
## >> 간단한 코드인데 너무 김. 간단하게 해줄수 있는 방법이 바로 '람다'.
# # 람다를 사용
# power = lambda 숫자: 숫자**2
# is_odd = lambda 숫자 : 숫자%2 ==1
# print(power(10)) #100
# print(is_odd(7)) #True

# #람다를 인라인 함수로 사용하기 (함수에 꽂아넣음)
# A=[1,2,3,4,5]
# 이터레이터 = map(lambda 숫자 : 숫자**2, A)
# print(list(이터레이터))

# 이터레이터 = filter(lambda 숫자: 숫자%2==1, A)
# print(list(이터레이터))

 #key키워드
A= [{
    "제목": "파이썬",
    "가격": 18000
},{
    "제목": "파이썬+자바",
    "가격": 26000
},{
    "제목": "파이썬+스파크",
    "가격": 20000
}]
print(min(A, key=lambda 북: 북["가격"]))
print(max(A, key=lambda 책: 책["가격"])["가격"]) #가격만 뽑고싶을때
#sort도 가능.
# 가격 상위 2개 항목
top_2 = sorted(A, key=lambda 책: 책["가격"], reverse=True)[:2]
print(top_2)

