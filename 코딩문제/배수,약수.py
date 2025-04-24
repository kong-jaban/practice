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

# #9506번 약수들의 합
# #완전수 구하기

# # 한줄간격 n받기
# # 마지막엔 -1로 종료

# while True:
#     A= int(input())
#     list= []
#     if A== -1 :
#         break
#     else:
#         for i in range(1, A):
#             if A%i ==0:
#                 list.append(i)
#     if sum(list) == A:
#         print(f'{A} =', ' + '.join(map(str, list)))
#     else: print(f'{A} is NOT perfect.')

# #소수찾기
# num = int(input())
# numbers = list(map(int,input().split()))

# count = 0
# for i in range(num):
#     result = []
#     for j in range(numbers[i]):
#         if numbers[i] % (j+1) == 0:
#             result.append(j+1)
#     if len(result) == 2:
#         count += 1

# print(count)

# #소수
# M = int(input())
# N = int(input())

# prime = []
# for num in range(M, N+1):
#     if num <2 :
#         continue
#     is_prime = True
#     for i in range(2, int(num**0.5)+1):
#         if num %i ==0:
#             is_prime=False
#             break
#     if is_prime:
#         prime.append(num)
# if prime:
#     print(sum(prime))
#     print(min(prime))
# else:
#     print(-1)

#소인수분해
N = int(input())
lst = []

i = 2
while i <= N:
    if N % i == 0:
        lst.append(i)
        N //= i  # 정수 나눗셈
    else:
        i += 1

print("\n".join(map(str, lst)))
#