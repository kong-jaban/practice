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

# # #####################################
# # 90강 - 모듈 만들기와 if __name__ == "__main__"
# #모듈 - 파일 또는 폴더를 활성해서 구성. 
# import sys
# print(sys.path)

# # #####################################
#  92강 - BeautifulSoup 외부 모듈(라이브러리) 사용해보기
#기본내장모듈 ex) math, sys, time
#외부모듈
# 터미널 : pip install 모듈이름
# pip install Flask
# pip install beautifulsoup4
# pip install tensorflow

# # 외부모듈을 찾는 방법 
# (1) 책에서 모듈 찾기
# 파이썬 웹프로그래밍 : Django, Flask
# 머신러닝 : scilit-learn, tensorflow
# 스크레이핑 : requests, beautifulsoup
# 영상분석 : cv2, pillow
# (2)파이썬 커뮤니티 가입
# > 인기 외부모듈 확인
# (3)그냥 검색

# # 간단예시 (beautifulsoup4, Flask)
# from bs4 import BeautifulSoup
# from urllib import request

# 기상청주소 = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon3rss_108_20250224.xml"
# 데이터 = request.urlopen(기상청주소)

# soup = BeautifulSoup(데이터, "html.parser")
# # soup.select()       #특정이름을 가진 태그를 모두 찾음
# # soup.select_one()   #특정 이름을 가진 태그 하나 찾음

# for location in soup.select('local_ta'):
#     city = location.select_one("local_ta_name").string
#     print(city)

# # #####################################
# # 93강 - Flask 외부 모듈(프레임워크) 사용해보기
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>안녕하세요!h1</h1>"

# @app.route("/introduce")
# def introduce():
#     return "<h1>저를 introduce합니다</h1>"
##플라스크에선 숫자로 시작할수 없음. 

# 라이브러리
#정상제어를 하는 모듈
#정상제어: 모듈의 기능을 개발자가 직접 호출하는 것
#(beautifulsoup)

# 프레임워크
#제어역전이 발생하는 모듈
#제어역전 : 모듈이 개발자가 만들 기능을 호출하는 것
#(flask)
