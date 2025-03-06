#     #10807번 개수세기
# N= int(input())
# numbers = list(map(int, input().split()))
# v = int(input())
# answer = 0
# for i in range(N):
#     if numbers[i] == v:
#         answer +=1
# print(answer)

    #10871번 X보다 작은 수
# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# C=[]
# for i in range(N):
#     if A[i] < X:
#         C.append(A[i])
# for j in range(len(C)):
#     print(C[j], end=" ")

    #2562번 최댓값 문제
# num_list = []

# for i in range(9):

#     num_list.append(int(input()))

# print(max(num_list))

# print(num_list.index(max(num_list))+1)

#     #10810번 #공넣기 문제
# 바구니 N개. 각 바구니에 1~N번호가 있음. 또 1~N번호가 적혀있는 공 많이있음.
# 처음바구니에는 공이 들어있지 않으며, 바구니에 공 1개만 넣을수 있음. 
# M번 공을 넣으려고 함. 
# 공넣을때 > 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공 넣음.
# 이미 공 있을 경우엔 안에있던 공 빼고 넣음. 바구니범위는 연속됨.
#바구니 범위=N, 넣는횟수=M
#i번바구니에서 j바구니까지 k번 번호 공 넣음. 
# N, M = map(int, input().split())
# lst = [0]*N
# for r in range(M):
#     i, j, k = map(int, input().split())
#     for m in range(i-1,j):
#         lst[m] = k
# print(*lst)

#     #10813번 공바꾸기
# N, M = map(int, input().split())
# lst=[i+1 for i in range(N)]
# trash= [0]*N
# # for m+1 in range(N):
# #     lst.append(m) #[1,2,3,4 ... N]
# for r in range(M):
#     i,j = map(int, input().split())
#     i-=1
#     j-=1
#     trash[j] = lst[j]
#     lst[j] = lst[i]
#     lst[i] = trash[j]
# print(*lst)

#     #5597번 과제제출
# l = [int(input()) for _ in range(28)]

# l.sort()
# l1 = list(range(1,31))
# l2 = []

# for i in range(len(l1)):
#     if l1[i] not in l:
#         l2.append(l1[i])

# for j in range(len(l2)):
#     print(l2[j], end ="\n")
 
# #10809번 알파벳 찾기
# s = input()

# for i in range(97, 123):
#   b = chr(i)

#   if b in s:
#     print(s.index(b), end = ' ')

#   else:
#     print(-1, end = ' ')

# p = [] 
# t = int(input())
# for _ in range(t):
#     r, s = input().split()
#     r = int(r)
#     for i in range(len(s)):
#         print(s[i]*r, end='')
#     print('')

# #1152번 단어 개수

# A=input()

# blk=0
# if A ==" ":
#     blk = 0
# elif A != " ":
#     A= A.strip()
#     blk= (A.count(" ")+1)
# print(blk)

# #2908번 상수
# #@@역순으로 출력
# # [::-1]
# #두가지 숫자 받기
# a,b = map(int, input().split(" "))

# #숫자 뒤집기
# a,b = (a[::-1]), (b[::-1])
# # print(a,b)
# #뒤집은 숫자 대소비교
# max_value = max(a,b)
# # #뒤집은 숫자 중 큰 숫자 출력
# print(max_value)
# @@@@역순출력은 str타입으로 변환 후 슬라이싱([::-1])하고 나서 다시 숫자 변환

# #5622번 다이얼 문제.
# A={
#     'ABC' : 3,
#     'DEF' : 4,
#     'GHI' : 5,
#     'JKL' : 6,
#     'MNO' : 7,
#     'PQRS': 8,
#     'TUV' : 9,
#     'WXYZ': 10
# }
# val = input()
# result = 0
# for i in val:
#     for key in A:
#         if i in key:
#             result += A[key]
# print(result)
# # #value부분에 있는지 확인할 경우 
# A = {
#     'ABC': 3,
#     'DEF': 4,
#     'GHI': 5
# }

# value_to_check = 4
# found = False

# for value in A.values():
#     if value == value_to_check:
#         found = True
#         break

# if found:
#     print("값이 있습니다.")
# else:
#     print("값이 없습니다.")

# #11718번 그대로 출력하기
# import sys

# # 여러 줄을 입력받아서 그대로 출력
# # sys.stdin.read()는 한 번에 여러 줄을 입력받을 때 유용합니다.
# input_data = sys.stdin.read()

# # # 그대로 출력
# # print(input_data)

