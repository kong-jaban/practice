#사칙연산
# # 1008번

# a,b = map(float, input().split())
# print(a/b)

# #2739번
# # N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# a=int(input())
# for i in range(1,10):
#     print(f"{a}*{i} = {a*i}")

# #10950번
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
# T=int(input())
# for i in range(1, T+1):
#     a,b = map(int, input().split())
#     print(a+b)

# #10925번
# 문제
# 준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.

# 출력
# 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.
# a=input()
# print(a+"??!")

# #18108번
# a= int(input())
# print(a-543)

# #10172번

# print("|\_/|")
# print('|q p|   /}')
# print('( 0 )""\'\\')
# print('|"^"`    |\n')
# print('||_/=\\\__|')

# # ++ '''로 감싸서 전체문장 가져오는 방법
# # ++ 특수문자 앞에 \붙여주면 문자로 인식함.
# # +줄바꿈 : \n

#######조건문########
# #9498번
# # 문제
# # 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# # 입력
# # 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# # 출력
# # 시험 성적을 출력한다.
# a= int(input())
# if a < 60 :
#     print('F')
# elif a < 70:
#     print("D")
# elif a < 80:
#     print("C")
# elif a < 90:
#     print("B")
# else :
#     print("A")

# #2753번 #윤달찾기
# a = int(input())
# if ((a % 100 != 0)or (a%400 ==0)) and (a%4 ==0):
#     print(1)
# else: print(0)

# #14681번 #사분면고르기
# a= int(input())
# b= int(input())

# if 1000>=a>0 :
#     if 1000>=b>0:
#         print(1)
#     elif 0>b>=-1000: print(4)
# elif 0>a>=-1000 :
#     if 1000>=b>0:
#         print(2)
#     elif 0>b>=-1000: print(3)

#2884번 #알람시계
# a,b = map(int,input().split())

# if (a != 0):
#     if b!=45: #a 0아니고 b 45아닐때
#         if 59>= b >45:
#             print(a, b-45)
#         elif 45> b >=0 :
#             print(a-1, 60-(45-b))
#     else : #a 0아니고 b 45일때
#         print(a, b-45)
# elif (a==0):
#     if b!=45: #a 0이고 b 45아닐때
#         if 59>= b >=45:
#             print(a, b-45) 
#         elif 45> b >=0:
#             print(23, 60-(45-b))
#     else: # a 0이고 b45일때
#         a==00
#         print(a, b-45)

#2525번 #오븐시계
a,b = map(int,input().split())
c = int(input())
#a가 0시로 넘어갈때
#a가 0시로 넘어가지 않을때
a = input()
b = int(input())
a = a.split()

i = int(a[0])
j = int(a[1])

x = b//60
y = b%60

if i + x >= 24:
    if j + y >= 60:
        print(i+x-24+1, j+y-60)
    else:
        print(i+x-24, j+y)
else:
    if j + y >= 60 and i + x + 1 >= 24:
        print(0, j+y-60)
    elif j + y >= 60:
        print(i+x+1, j+y-60)
    else:
        print(i+x, j+y)
    
    