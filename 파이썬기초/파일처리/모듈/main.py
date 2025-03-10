# #90강
# import hellomodule
# # print(hellomodule.a)
# # print(hellomodule.b)
# # print(hellomodule.C)
# print(hellomodule.Circle(10))

# from hellomodule import Circle
# # print(Circle().넓이(5)) #안됨
# print(Circle(5).둘레()) #됨

# print("#main")
# print(__name__) #__main__ #메인아닐경우 __없음

# # if __name__ == __main__ 조건문

# if __name__ =="__main__":
#     print("##넓이()검증시작")
#     if Circle(10).넓이() - 314 < 10**7:
#         print("넓이 검증 성공!:Success")
#     else : print("넓이가 다릅니다: Fail")
#     Circle(10).둘레() == 356
# #이 파일이 메인으로 실행되었는지에 대한 조건문임.

# 91강 - 패키지 기본
# 패키지 : 모듈의 규모가 커졌을 때 그 모듈을 나누는 방법.
# 모듈 : 관심사를 기반으로 함수와 변수를 나누는 것

# # 1. 폴더 내부에 있는 모듈을 읽어들이는 방법 (school 폴더)
# from school.student import Student
# from school.studentlist import StudentList
# sl=StudentList()
# sl.append(Student(100))
# sl.append(Student(80))
# sl.append(Student(50))
# sl.print()

# # 2. 폴더 자체를 모듈로 읽어 들이는 방법
# import school

# print(school.a)
# school.b()
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>안녕하세요!h1</h1>"

@app.route("/introduce")
def introduce():
    return "<h1>저를 introduce합니다</h1>"