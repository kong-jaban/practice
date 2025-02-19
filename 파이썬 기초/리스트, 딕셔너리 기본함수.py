# a= [52,263, 32, 103,53]
# print(max(a))
# print(min(a))
# print(max(*a))
# print(sum(a))
# a= range(0,10)
# for i in reversed(a):
#     print(i)

# #enumerate() 함수
# fruits = ["바나나", "사과", "포도"]
# i =0
# for fruit in fruits:
#     print(fruit)
# #enumerate() 사용시 > [(), (), ()] 형태 (튜플)
# # 튜플 내부의 형태는 [(인덱스, 값),(인덱스, 값)]
# for fruit in enumerate(fruits):
#     print(fruit[0], fruit[1])

# # 형식 
# # for 인덱스, 값 in enumerate(리스트)
# for i, fruit in enumerate(fruits):
#     print(i, fruit)


# #items()함수
# a= {
#     "이름":"바나나",
#     "가격": 1500,
#     "원산지":"말레이시아"

# }
# for k, v in a.items():
#     print(k, v)

######
#리스트 내포(List comprehension)
#반복가능한 것을 기반으로
#새로운 리스트를 만들어내는 문법
#An = 2n+1 (0<= n < 10)
#A = {1,3,5,7,9,...19}
A=[]
for i in range(0, 10):
    A.append(2*i +1)
print(A)
# >>리스트 내포로 변환하면? >
#형식 = [표현식 for 반복]
A = [(2*i+1) for i in range(0,10)]
print(A) #같은결과

# 다른형식
A=[
    2 * i +1                #표현식
    for i in range(0,10)    #반복문
    if (i % 2== 0)          #조건문
    
]
print(A)