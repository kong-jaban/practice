# #5086번 배수와 약수 

# while True:
#     A, B = map(int, input().split())
#     if A==0 and B==0:
#         break

#     if B%A == 0:
#         print("factor")
#     elif A%B ==0:
#         print("multiple")
#     else: print("neither")

# #2501번 약수구하기
# #N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력
# a,b = map(int, input().split())
# list=[]

# for i in range(a+1):
#     if i == 0:
#         continue
#     else:
#         if a%i==0:
#             list.append(i)
# if b>len(list):
#     print(0)
# else: print(list[b-1])

#9506번 약수들의 합
#완전수 구하기

# 한줄간격 n받기
# 마지막엔 -1로 종료

while True:
    A= int(input())
    list= []
    if A== -1 :
        break
    else:
        for i in range(1, A):
            if A%i ==0:
                list.append(i)
    if sum(list) == A:
        print(f'{A} =', ' + '.join(map(str, list)))
    else: print(f'{A} is NOT perfect.')