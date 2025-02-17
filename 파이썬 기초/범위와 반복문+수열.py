#범위
# 특정한 범위 내부의 정수들을 나열하는 자료형

# (1) range(A) #매개변수 1개넣는 경우
# 0부터 A까지의 정수를 범위로 나열
# A는 포함하지 않음.
# 특정 횟수만큼 반복하는 경우

# (2) range(A, B) #매개변수 2개넣는 경우
# A부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음
# 반복변수를 사용하는 경우

# (3) range(A, B, C) #매개변수 3개넣는 경우
# A부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음
# C만큼씩 건너뛰면서 범위를 생성
# 반대로 반복하는 경우. (10, -1, -1)

# # 반복문에 적용이 가능함. 
# for i in range(10, 0, -1):
#     print(f"{i}번째") # 0~9 출력

# 수열
# a_n = 2*n-1
# 쭉 나열하고싶다면?
# a=[None]
# for n in range(1, 101):
#     a_n = 2*n-1
#     a.append(a_n)
# print(a)

# # 점화식 (이전항을 기반으로 다음항을 만듦)
# a=[None]
# for n in range(1, 11):
#     if n ==1:
#         a_n=1
#     else:
#         a_n = a[n-1] +2
#     a.append(a_n)
# print(a)

# 특정 길이의 리스트 만들기
#append 기능은 파이썬에서 느림. (리스트 길이 확장)
# print([0] * 10) #10개의 리스트 길이를 가진 리스트 만들수있음.
# #응용
# N=100
# a=[None] * (N+1)
# for n in range(1, N+1):
#     if n ==1:
#         a[1]=1
#     else:
#         a[n] = a[n-1] +2 #동적계획법. (이전항을 이용해서 표현)
# print(a)

#피보나치수열 구하기
N=100
a=[None] * (N+1)
for n in range(1, N+1):
    if n ==1 or n==2:
        a[n]=1
    else:
        a[n] = a[n-1] +a[n-2] #동적계획법. (이전항을 이용해서 표현)
print(a)