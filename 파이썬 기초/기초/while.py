# while 반복문
# if조건문과 비슷
# while True: #or False
#     #복합구문
#     #조건이 참이라면 반복
#     print(".")

# 기본 예시
# i = 0
# while i <100:
#     print(f"{i}번째 반복중")
#     i += 1

#while 은 언제 사용하는가??
# 숫자로 반복하는 것이 아닐 때

# #ex1) 2가 없어질때까지 반복
# a=[1,2,1,2,3, 2]
# value =2
# while value in a:
#     a.remove(value)
#     print(a)

#ex 2) 시간의 경과
import time
시작시간 = time.time()
현재시간 = time.time()

while 현재시간 < 시작시간 + 5:
    print(현재시간, 시작시간 +5)
    현재시간 = time.time()