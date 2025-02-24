# 문제
# 단어 
# $S$와 정수 
# $i$가 주어졌을 때, 
# $S$의 
# $i$번째 글자를 출력하는 프로그램을 작성하시오.

# a = input()
# b= int(input())
# print(a[b-1])

# #   #단어길이 세기
# a=input()
# print(len(a))

#첫글자,마지막글자 출력
s=int(input())
for _ in range(s):
  s = input()
  print(s[0]+s[-1])

