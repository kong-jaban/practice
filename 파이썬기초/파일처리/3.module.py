#카테고리로 구분하기 위해서
##클래스 : 객체라는 주어로 묶는 방법
##모듈 : 관심사를 기반으로 묶는 방법
# ex) 수학관련대상 > math모듈
#     랜덤처리관련대상 > random 모듈
#     시스템관련대상 > sys모듈
#모듈의 기본적인 활용방법
# A)내가 무엇을 해야하는가? 인지하기
# B)구글에서 찾은뒤 사용

#1. 기본적인 모듈

#읽는 방법
# #   1) import 모듈 > 모듈을 식별자로 읽어들임
# import math
# print(math.sin(1))
# print(math.cos(1))
# print(math.ceil(3.5))
# print(math.floor(3.5))
# #   2) import 모듈 as A
# #   모듈을 A라는 식별자로 읽어들임
# import math as m
# m.sin(1)
# m.cos(1)
# #   3) from 모듈 import 변수, 함수, 클래스
# #   "변수, 함수, 클래스"를 모듈로 읽어들임
# from math import sin, cos, tan
# sin(1)
# cos(1)
# tan(1)

# #파이썬 문서에서 모듈 살펴보기!!
# import sys
# import os 
# import time
# from urllib import request #웹관련

# time.sleep(5)
# print(sys.argv)
# target = request.urlopen("https://google.com")
# print(target.read())
#2. 외부모튤 설치
#3. 모듈 만들기

# #####################################
# import os
# output = os.listdir(".")
# print("os.listdir():", output)
# print()
# print("@폴더와 파일 구분@@")
# for i in output:
#     if os.path.isdir(i):
#         print("폴더:", i)
#     else:
#         print("파일:", i)

# #재귀함수로 모든 파일 탐색(폴더라면 또 탐색하기)
# import os

# def read_folder(path):
#     #폴더 요소 읽기
#     output = os.listdir(path)
#     #폴더 요소 구분하기
#     for item in output:
#         if os.path.isdir(item):
#             read_folder(path + "/" + item)
#         else:
#             print("파일:", item)
# read_folder(".")

# #####################################
# 90강 - 모듈 만들기와 if __name__ == "__main__"
#모듈 - 파일 또는 폴더를 활성해서 구성. 
import sys
print(sys.path)