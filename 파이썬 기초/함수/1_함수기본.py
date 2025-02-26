#50강
#매개변수 : 함수의 괄호 안에 넣는 변수
## parameter : 함수 정의 때 넣은 변수
###함수를 설계하는 사람
    #1. 함수의 설명서 (documentation)
    #2. 예외처리
# def print_3_times(문자열, 횟수):
#     for i in range(횟수):
#         print(문자열, i, sep="")
# ## argument : 함수 호출 때 넣은 값
# print_3_times("안녕", 10)
# 안녕0
# 안녕1
# 안녕2 ...
###############################
#51강
#가변 매개변수 함수
# def print_n_times(횟수, 출력대상, 출력대상, ...):
#     for i in range(횟수):
#         print(문자열, i, sep="")
#   를 표현하고자 함. 
# def print_3_times(횟수, [리스트]): -->>
# def print_3_times(횟수, *리스트): # 리스트 앞에 *븥이면 리스트 풀리고 괄호안에 들어감. (튜플)
#     for i in range(횟수):
#         for 요소 in 리스트:
#             print(요소)
###############################
#52강
# #기본 매개변수
# def test(a=10):
#     print(a)
# test()      #10
# test(20)    #20
# test(a=30)  #30
#     #두개이상일때
# def test(a=20, b=30):
#     print(a,b)
# test()      #20 30
# test(10)    #10 30
# test(a=40)  #40 30
# test(b=50)  #20 50 

#     #딕셔너리 매개변수
# def 함수(*가변, **딕셔너리):
#     print(가변, 딕셔너리)
# 함수("안", "녕", "하", a=10, b=20, c=30)

###############################
#53강
#리턴?
# > 함수에서 어떠한 값을 가지고 나갈 것인지!!
#   (값을 들고 돌아가라.return)
# 리턴 뒤에 아무것도 안쓰면 return None

# #기본형식
# def 함수(매개변수):
#     변수= 초기화
#     #여러가지 처리
#     #여러가지 처리
#     return 변수

# #예제
# def sum_all(start, end):
#     output = 0 #항등원으로 초기화
#     for i in range(start, end+1):
#         output+= i
#     return output
# print(sum_all(1,1000))

##################################
#54강 메모리 구조
#자료구조 => 스택과 힙 : 너무 유용함.!

#자료를 크게 2가지로 구분
#(1)기본 자료형 : 숫자, 문자열, 불 등
#(2)복합 자료형 : 리스트, 딕셔너리, 객체 등
#기본 자료형 차곡차곡 저장되어있는곳 > '스택'
#복합자료형은 '힙'이라는 창고에 저장해놓고 어떤위치에 저장했는지를 '스택'에 기록함.
# #기본
# a=10
# b=True
# c="안녕하세요"
# #복합
# d= [1,2,3,4]
# e={"이름": "구름", "나이":8}

# #할당과 참조
# a=10
# b=[1,2,3,4]
# def function():
#     a=20
#     b=[5,6,7,8]
#     print(a) #20
#     print(b) #[5,6,7,8]
# function()
# print(a) #10
# print(b) #[1,2,3,4]
# #함수는 자신과 가까운 스택에서 참조함. 

##################################
#55강 메모리구조(2) : global 키워드

#global키워드 사용하는 이유
# 함수에서는 실행될때 변수를 찾는 과정을 가짐. 내부에서 변수를 찾았는데
# 실행되는 코드가 변수 선언보다 빠를 경우 아직 선언 전이어서 그 변수를 가져올 수 없음.
# >이럴 경우 global 키워드를 통해 외부의 변수를 가져올 수 있음. 

#이외에
# a=10
# b=[1,2,3,4]
# def function():
#     a=20

#     # b=[5,6,7,8] #함수스택에 새로운 변수를 만듬
#     b.extend([5,6,7,8]) #함수 스택에 새로운 변수를 만드는 것이 아님. 

#     print(a)
#     print(b) #extend 경우 1~8
# function()
# print(a)
# print(b)

##################################
# #56강 메모리 구조(3) : 복사
# a= 10
# b= [1,2,3,4]
# def function_a(c,d):
#     c=20
#     d=[5,6,7,8]
# function_a(a,b)
# print(a,b)
# def function_b(c,d):
#     c=30
#     d.extend([9,10])
# function_b(a,b)
# print(a,b)
##################################
# #57강 재귀함수(1) : 기본
# def factorial(n):
#     if n == 1:
#         return 1
#     elif n>= 2:
#         return n*factorial(n-1) #함수 내부에서 함수를 호출(재귀함수)
# print(factorial(5))

#58강 재귀함수(2) : 피보나치 수열
#피보나치수열
# a_1=1
# a_2=2
# a_n=a_{n-1} +a{n-2}
#함수로 표현하면>>
# def f(n):
#     if n ==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# print(f(50))
# > 실행 굉장히 느림.. n-1과 n-2를 구하고 그에 해당하는 값에도 각각 n-1과n-2를 구해야하기 때문..
#쓸데 없는 계산이 많음. 중복계산도 많음..

# #메모화 : memo에 값을 저장해서 중복되는 계산을 없앨 수 있음. 
# memo={1:1, 2:1} #1,2번째 항은 1인것을 미리 입력. 밑에 if문 줄일수있음. 
# # memo={}
# def f(n):
#     if n in memo:
#         return memo[n]
#     # if n ==1:
#     #     return 1
#     # elif n==2:
#     #     return 1
#     else:
#         temp = f(n-1)+f(n-2)
#         memo[n]= temp
#         return temp
# print(f(50))
##################################
#59강 - 조기리턴과 평탄화
data = [[1,2,3],[4,[5,6]],7,[8,9]]
def flatten(data):
    output = []
    for item in data:
        if type(item) ==list :
            output.extend(flatten(item)) #재귀함수로서 기능
        else:
            output.append(item)
    return output
print(flatten(data))