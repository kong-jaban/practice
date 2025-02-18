# break 키워드
# > 반복문 전체를 벗어날때 사용하는 구문

# i = 0
# while True :
#     print(f"{i+1}번째반복")
#     i += 1

#     a = input(">종료하시겠습니까? (y/n)")
#     if a in ["y", "Y"]:
#         print("종료합니다")
#         break

# continue 키워드
# >현재 반복을 넘어갈때 사용하는 구문

# numbers = [5,15,6,20,7,25,30]

# for i in numbers :
#     # if i >= 10:
#     #     print(i)
#     if i <10:
#         continue 
#     print(i)


#####확인문제#####
# #1) 리스트조합해서 딕셔너리 만들기
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]

# character = {}

# for i in range(0,4):
#     character[key_list[i]] = value_list[i]
# print(character)

# #2) 1부터 하나씩 증가해서 더하는 경우에 1)몇을 더할때 1000을넘는가? 2)그때의 값
# # ex) 1, 1+2=3, 1+2+3=6, 1+2+3+4=10 ..
# i = 1
# limit = 10000
# sum_value= 0
# while sum_value <= limit:
#     sum_value += i
#     i+=1
# print(f"{i-1}를 더할때 {limit}을 넘으며 그때의 값은 {sum_value}")

# 3) 1부터 100까지 있을때 최대가 되는 경우는?
 #ex) 1*99, 2*92, 3*97 ...

# #풀이 1)
# a = []
# for i in range(1, 100):
#     j= 100-i
#     a.append([i,j, i*j])
# # print(a)
# max_list=a[0]
# now_max = max_list[2]
# for i in a:
#     if now_max < i[2]:
#         max_list = i
#         now_max = max_list[2]
# print(max_list)

# #풀이 2)
# max_value= 0
# a=0
# b=0
# for i in range(1, 100):
#     j = 100-i
#     if max_value < i*j:
#         max_value = i*j
#         a=i
#         b=j
# print(f"{a}와{b}를 곱했을때 {max_value}가 최대입니다.")