# # 반복문, 함수가 어려운 이유?
# #  -위에서 아래로 내려오는 구조가 아님. 

# 수열 = 수의 나열 (인덱스 1부터 시작)
# 배열 : 수열과 비슷하지만 (인덱스 0부터시작함.)
#  -형태는 []로 둘러쌓여있음.
#  - 길이가 고정되어있음. 
# 리스트 : 배열에 요소 추가/제거 등의 기능을 추가한 것
# ex) a= [123, "abc", True]
# a[0] = 123 , a[1]="abc"
# a[0:2]= [123, "abc"]
# len(a) = 3
# a[start:end:step] > 리스트 호출방법
# a[::-1] > 리스트 반대로 돌리기
# #중첩리스트
# b= [[1,2,3], [4,5],[6,7]]
# b[0] #[1,2,3]
# b[0][0] #1

# ##배열과 쓰는 함수
# # 요소 추가: append(), insert(), extend()
# a= [1,2,3,4]

# a.append(10)#가장 마지막에 원하는 요소 하나 추가
# print(a) # [1,2,3,4,10]

# a.insert(0, 20) #원하는 위치에 요소 하나를 추가
# print(a) #[20,1,2,3,4,10]

# a.extend([5,6,7,8]) #가장 마지막에 요소를 여러개 추가
# print(a) #[20,1,2,3,4,10,5,6,7,8]
#  # a=a+[5,6,7,8]

# # 요소 제거: del, pop(), remove(), clear()

# a=[1,2,3,4,5,6,7]
# del a[0] #제거하고 싶은 인덱스 입력
# print(a) #[2,3,4,5,6,7]

# a.pop() #제거하고싶은 인덱스 입력 (기본값 -1)
# print(a) #[2,3,4,5,6]

# a.remove(3) #제거하고싶은 요소를 입력
# print(a) #[2,4,5,6] #3이 제거됨

# a.clear()
# print(a) #[]

# # 요소 정렬: sort()
# a= [52, 372, 9, 7, 103, 13, 501, 231]

# a.sort()
# print(a) #오름차순 출력

# a.sort(reverse=True)
# print(a) #내림차순 출력


# # 요소 존재 확인: in, not in
# print(52 in a) #True
# print(0 in a) # False
# print(52 not in a) #False

# for 반복문
# 형태 -> for 반복변수 in 리스트:
#           복합구문
 #반복변수 에 a의 요소가 하나하나 들어감. 

# a= [1,2,3,4,5]
#     #총합 구하기
# sum=0 #더할 변수 초기화 /선언
# for i in a:
#     sum = sum + i
# print(sum)
#     #총곱 구하기
# prod=1 #곱할 변수 초기화/선언
# for i in a:
#     prod = prod * i
# print(prod)

# 중복리스트
# #2차원리스트
# a= [[1,2,3],[4,5,6,7],[8,9]]
# for i in a:
#     print(i)
#     for j in i:
#         print(j)

# # 전개연산자
# # *리스트 = 요소,요소,요소
# ## (1)리스트 내부
# a=[1,2,3]
# b=[*a, *a, *a] #[1,2,3,1,2,3,1,2,3]
# print(b)
# #append활용
# a = [1,2,3]
# b=[*a, 4] #[1,2,3,4]

# ## (2) 함수의 매개변수 위치
# date= [2022, 8, 10,14,14]
# print("{}년{}월{}일{}시{}분".format(*date))

# list_a = [1,2,3,4]
# list_a.extend(list_a*2)
# print(list_a)# [1,2,3,4,1,2,3,4,1,2,3,4]

# numbers= [273, 103, 5,32, 62, 90,9, 72, 900]
# #100이상의 수
# for number in numbers:
#     if number > 100:
#         print(number)
        
# for number in numbers:
#     if number %2 == 0:
#         print(f"{number}은/는 짝수입니다.")
#     else : print(f"{number}은/는 홀수입니다. ")
#     print(f"{number}은/는 {len(str(number))}자리수입니다.")

# # 나머지값으로 주기성 만들기
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]
# for number in numbers :
#     output[(number-1)%3].append(number)
# print(output)

####################################
# #4-2 딕셔너리
# product = {
#     # 키: 값,
#     # 키: 값,
#     # 키: 값 ...
#     "제품명": "건망고 슬라이스",
#     "가격": 4000,
#     "분류": "식품",
#     10: 20
# }
# print(product["가격"],product["제품명"], product[10])

#  ##딕셔너리에 추가/제거
# product = {
#     "name": "7D건조망고",
#     "type": "당절임"
# }
# # 요소의 값을 변경
# product["name"] = "8D건조망고"
# # 요소를 추가
# product["price"] = 8000
# # 요소 제거
# del product["type"]
# # 키의 존재를 확인하기
# #  #get()
# print("type" in product)
# print(product.get("name"), product.get(type)) #없을경우 None을 출력
# print(product)
# for products in product:
#     print(products) #key값들이 출력됨. 

#  ##for 반복분 딕셔너리ver.
# for key in product:
#     print(key)
#     print(product[key])
#     print("-"*20)

# #문제풀이
# #1. 숫자가 몇번 등장하는지 출력하는 코드
# numbers= [1,2,6,8,4,3,2,1,9,4,5,4,6,8,9,1,3,5,7,3,3,4]
# counter= {}
# #(1) 요소의 출현을 확인
# for number in numbers:
#     counter[number] = 0 #counter딕셔너리 만들어주는 작업. 아무것도 없는곳에 1을 더할수 없어..
# #(2) 해당 요소의 빈도를 확인
# for number in numbers :
#     counter[number] += 1
# #(1), (2) 결합
# for number in numbers:
#     if number not in counter:
#         counter[number] =0
#     counter[number] += 1
# print(counter)
# #정렬까쥐
#    #키 기준 정렬
# for key in sorted(counter.keys()):
#     print(f"{key}: {counter[key]}")
#    #value 기준 정렬 @@@미숙@@@
# for key, value in sorted(counter.items(), key=lambda x:x[1]):
#     print(f"{key}: {value}")

#활용예제. (딕셔너리 내부 딕셔너리, 리스트 등)
#딕셔너리
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃검",
        "armor": "풀갑옷"
    },
    "skills": ["베기", "종베기", "횡베기"]
}
# for 반복문으로 나열
for key in character:
    if type(character[key]) is dict: #요소가 딕셔너리타입일때
        # print(character[key])
        for 키 in character[key]:
            print(f"{키} : {character[key][키]}") #한번더 요소접근
        # for 키, 값 in character[key].items():
        #     print(f"{키} : {값}")     #위 코드와 동일한 결과
        
    elif type(character[key]) is list: #요소가 리스트일때
        for 요소 in character[key]:
            print(f"skills : {요소}")
    #딕셔너리일때와 리스트 일때 차이?
    #딕셔너리반복문에서는 반복 변수에 키가 들어감. 
    #리스트에서는 반복 변수에 요소 자체가 들어감.
    else:
        print(f"{key} : {character[key]}")
