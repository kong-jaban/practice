############################
#79강 - 클래스 등장 이전
#문제(1) 어떤 함수가 있는지 자체를 모를 수 있다.
#문제(2) 변수에 직접적으로 접근 할 수 있다.
#문제(3) 함수가 분산되어 있다.
# >>클래스로 해결이 가능함. 

#80강 - 클래스 문법 기본
#클래스 : 함수(와 변수)를 묶어 놓은 것. 
# ->객체를 만들어내기 위한 설계도 

# #클래스(설계도)
# 학생
#     이름
#     국어
#     영어
#     수학
#     과학 ..

# #객체 = 인스턴스 (설계대로 만든 놈)
# "성렬", 89, 92, 92,19
# "수정", 84,95,96,84
# "병준", 84,54,75,65
    #######

# #클래스 사용
# class 학생 :
#     #클래스의 내용
#     pass
# #객체
# 성렬 = 학생()

# #변수추가
# 성렬.이름= "성렬"
# 성렬.국어= 95
# 성렬.영어 = 84
# 성렬.수학 = 51
# 성렬.과학= 95

# print(성렬.수학) #51
    #########
# #클래스(설계도)
# class Student:
#     #클래스의 내용
#     # def 초기화(self,이름,국어,영어,수학,과학): #클래스가 갖는 모든 함수는 첫번째 매개변수로 self를 가져야 함.
#     #                   #(클래스함수 제외)
#     #     self.이름=이름
#     #     self.국어=국어
#     #     self.영어=영어
#     #     self.과학=과학
#     #     self.수학=수학
#     def __init__(self,이름,국어,영어,수학,과학):
#         #객체에 매개변수 직접전달 가능(?)
#         self.이름=이름
#         self.국어=국어
#         self.영어=영어
#         self.과학=과학
#         self.수학=수학
#     def sum(self):
#         return self.국어+ self.수학+self.과학+self.영어
#     def average(self):
#         return self.sum()/4
# #객체(인스턴스)
# 성렬=Student("성렬", 87,88,98,95)
# 영훈=Student("영훈", 87,95,98,97)

# #함수호출방법 (1)
# Student.초기화(성렬, "성렬", 87,88,98,95)
# print(성렬.이름,성렬.국어)
# #함수호출방법 (2)
# 성렬.초기화("성렬", 87,88,95,32)
# print(성렬.이름, 성렬.국어)
# print(영훈.sum(), 영훈.average())

###################################
# #81강 - 특수한 이름의 함수, 값 객체
# # 여담: 사실 비교 연산자로 "학생의 성적을 비교할 것이다"는 의도를 알아채기 힘듭니다.
# # 그래서 이런 식으로 구현하시면 안 됩니다[그냥 예입니다]. 아래 값 객체 예처럼 사용해주세요.
# class Student:
#     def __init__(self, 이름, 국어, 영어, 수학, 과학):
#         self.이름 = 이름
#         self.국어 = 국어
#         self.영어 = 영어
#         self.수학 = 수학
#         self.과학 = 과학
#     def sum(self):
#         return self.국어 + self.수학 + self.영어 + self.과학
#     def average(self):
#         return self.sum() / 4
#     def print(self):
#         print(self.이름, self.sum(), self.average(), sep="\t")
#     def __str__(self):
#         return f"{self.이름}\t{self.sum()}\t{self.average()}"
#     def __eq__(self, 다른대상): # self == 다른대상
#         if type(다른대상) == Student:
#             return self.sum() == 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() == 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"
#     def __ne__(self, 다른대상): # self != 다른대상
#         if type(다른대상) == Student:
#             return self.sum() != 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() != 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"
#     def __gt__(self, 다른대상): # self > 다른대상
#         if type(다른대상) == Student:
#             return self.sum() > 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() > 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"
#     def __ge__(self, 다른대상): # self >= 다른대상
#         if type(다른대상) == Student:
#             return self.sum() >= 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() >= 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"
#     def __lt__(self, 다른대상): # self < 다른대상
#         if type(다른대상) == Student:
#             return self.sum() < 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() < 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"
#     def __le__(self, 다른대상): # self <= 다른대상
#         if type(다른대상) == Student:
#             return self.sum() <= 다른대상.sum()
#         elif type(다른대상) == int:
#             return self.sum() <= 다른대상
#         else:
#             raise "같은 자료형을 비교해주세요"

# class StudentList:
#     def __init__(self):
#         self.__students = []
#     def add(self, student):
#         self.__students.append(student)
#     def print(self):
#         print("이름", "총점", "평균", sep="\t")
#         for student in self.__students:
#             student.print()
#     def __str__(self):
#         output = "이름\t총점\t평균\n"
#         for student in self.__students:
#             output += f"{str(student)}\n"
#         return output.strip()
#     def clone(self): #비파괴적으로 +=연산자 사용하기 위해 생성(자기자신 복제)
#         output = StudentList()
#         for student in self.__students:
#             output.add(student)
#         return output
#     def __add__(self, 다른대상):
#         output = self.clone()
#         output.add(다른대상)
#         return output

# students = StudentList()
# students += Student("인성", 87, 88, 98, 95)
# students += Student("구름", 92, 98, 97, 98)
# students.add(Student("별이", 76, 96, 95, 90))
# print(students)

# # 값 객체 예
# class CmLength:
#     # 유효한 값만 객체로 만들게 조건문을 걸었습니다.
#     def __init__(self, cm):
#         if cm < 0:
#             raise "길이는 0 이상으로 지정해야 합니다."
#         self.__length = cm
#     # 이게 뭔지는 다다음 강의에서 자세하게 다루겠습니다.
#     def get():
#         return self.__length
#     # __sub__, __mul__, __truediv__, __floordiv__ 등도 비슷하게 구현하면 됩니다.
#     def __add__(self, 다른대상):
#         if type(다른대상) != CmLength:
#             raise "길이 단위를 통일해주세요!"
#         return CmLength(self.get() + 다른대상.get())
#     # 다른 비교 연산자도 다음과 비슷하게 구현하면 됩니다.
#     def __eq__(self, 다른대상):
#         if type(다른대상) != CmLength:
#             raise "같은 자료형끼리만 비교할 수 있습니다."
#         return self.get() == 다른대상.get()
#     def __ne__(self, 다른대상):
#         return not (self == 다른대상)

# CmLength(3) + CmLength(10)

###########################
# # 82강 - 캡슐화
# # """변수와 함수를 숨겨서
# # 클래스 사용자가 객체를
# # 안전하게 사용할 수 있게 만드는 것"""
# # 변수와 함수를 훔기는 작업.
# # 인스턴스 변수와 인스턴스 함수 앞에 __를 붙이면
# class Circle:
#     def __init__(self,반지름):
#         if 반지름 <0: 
#             raise TypeError("반지름은 0이상이어야합니다.")
#         self.__반지름=반지름 #__를 붙여서 외부에서 접근하지 못하게 함. 
#         self.__파이=3.14
#     def get_반지름(self):
#         return self.__반지름
#     def set_반지름(self,value):
#         if value <0:
#             raise TypeError("반지름은 0이상이어야합니다.")
#         self.__반지름 = value
#     def 둘레(self):
#         return 2*self.__파이*self.__반지름
#     def 넓이(self):
#         return self.__파이*(self.__반지름**2)
# # circle= Circle(-10)
# circle= Circle(30)
# print(circle.get_반지름())
# print(circle.둘레())#둘레구함
# print(circle.넓이()) #넓이 구함
# circle.set_반지름(50)
# print(circle.둘레())#둘레구함
# print(circle.넓이()) #넓이 구함
# print(circle.get_반지름())

# #circle.둘레 하면 바로 나와야지!! 해서 만드는게 바로 "프로퍼티".
# # @property ->를 함수 위에 적으면 ()없이 호출.

##########################
# #  83강 - 상속 기본
# #상속? > 여러 클래스에 공통적으로 포함되어있는부분을 따로구현하는 것. 
# # 상속
# class Shape: #부모클래스
#     def __init__(self):
#         raise "생성자를 구현해주세요."
#     def 넓이(self):
#         raise "넓이 함수를 구현해주세요. 넓이를 리턴하는 함수를 작성해주세요."
#     def 출력보조(self):
#         raise "출력 보조 함수를 구현해주세요. 출력 전 한마디를 입력해주세요."
#     def 출력(self):
#         print("=" * 10)
#         print("!" * 10)
#         print("=" * 10)
#         self.출력보조()
#         print(f"넓이: {self.넓이()}")
#         print("=" * 10)
#         print("!" * 10)
#         print("=" * 10)

# class Circle(Shape): #자식클래스 ()안에 부모클래스
#     def __init__(self, 반지름):
#         self.파이 = 3.14
#         self.반지름 = 반지름
#     def 출력보조(self):
#         print(f"원의 반지름은 {self.반지름}")
#     def 넓이(self):
#         return self.반지름 * self.반지름 * self.파이

# class Square(Shape): #자식클래스 ()안에 부모클래스
#     def __init__(self, 길이):
#         self.길이 = 길이
#     def 출력보조(self):
#         print(f"정사각형 한 변의 길이는 {self.길이}")
#     def 넓이(self):
#         return self.길이 * self.길이

# square = Square(10)
# square.출력()
#########################
#84강 - 오버라이드와 super() 함수
#오버라이드(override()) > 재정의
# class 부모:
#     def 함수(self):
#         print("부모의 함수입니다.")

# class 자식(부모):
#     def 함수(self):
#         super().함수() #부모함수 출력

#         print("자식의 함수입니다.") #자식함수 출력
#         # 1
#         부모.함수(self) #부모함수 출력
#         # 2
#         super().함수() #부모함수 출력
# child=자식() 
# child.함수()
# ###
# class 빨간버튼:
#     def __init__(self):
#         print("버튼 초기화")
#         print("버튼 만들기")
#         print("버튼화면에 출력")
#         print("버튼 빨간색으로 칠하기")
# class 파란버튼:
#     def __init__(self):
#         print("버튼 초기화")
#         print("버튼 만들기")
#         print("버튼화면에 출력")
#         print("버튼 파란색으로 칠하기")
# class 초록버튼:
#     def __init__(self):
#         print("버튼 초기화")
#         print("버튼 만들기")
#         print("버튼화면에 출력")
#         print("버튼 초록색으로 칠하기")
# 빨간버튼()
# 파란버튼()
# 초록버튼()
# # >> 공통처리>부모클래스로 바꾸기
# class 버튼:
#     def __init__(self):
#         print("버튼 초기화")
#         print("버튼 만들기")
#         print("버튼화면에 출력")   
# class 빨간버튼(버튼):
#     def __init__(self):
#         super().__init__()
#         print("버튼 빨간색으로 칠하기")
# class 파란버튼(버튼):
#     def __init__(self):
#         super().__init__()
#         print("버튼 파란색으로 칠하기")
# class 초록버튼(버튼):
#     def __init__(self):
#         super().__init__()
#         print("버튼 초록색으로 칠하기")
# 빨간버튼()
# 파란버튼()
# 초록버튼()
#############################
# #85강 - 상속과 컴포지션
# # 위험성 많음.
# #방대한 양의 클래스를 상속받음 > 위험요소 숨길것 많음.(블랙리스트)
# # > 이것보다 많은요소를 갖는 클래스를 캡슐화로 숨기고 필요한 요소만 공새하는것
# # (화이트리스트)가 더 쉬움
# class Student:
#     def __init__(self, 수학):
#         self.수학= 수학
# class StudentList(list):
#     def append(self, 요소):
#         if type(요소) != Student:
#             raise "Student를 전달해주세요."
#         super().append(요소)
#     def sum(self):
#         output=0
#         for 학생 in self:
#             output += 학생.수학
#         return output
#     def average(self):
#         return self.sum() / len(self)
# 학생목록 = StudentList()
# 학생목록.append(Student(100))
# 학생목록.append(Student(80))
# 학생목록.append(Student(50))
# for 학생 in 학생목록:
#     print(학생.수학)
# print(학생목록.sum())
# print(학생목록.average())
# #위 코드를 숨기기(컴포지션)
# class Student:
#     def __init__(self, 수학):
#         self.수학= 수학
# class StudentList(list):
#     def __init__(self):
#         self.__리스트= []
#     def append(self, 요소):
#         if type(요소) != Student:
#             raise "Student를 전달해주세요."
#         self.__리스트.append(요소)
#     def sum(self):
#         output=0
#         for 학생 in self.__리스트:
#             output += 학생.수학
#         return output
#     def average(self):
#         return self.sum() / len(self.__리스트)
# 학생목록 = StudentList()
# 학생목록.append(Student(100))
# 학생목록.append(Student(80))
# 학생목록.append(Student(50))

# print(학생목록.sum())
# print(학생목록.average())

#상속 :프레임워크가 상속을 강제한다면 > 상속
#컴포지션 : 일반적인 경우
#################
# 86강 - 컴포지션으로 스택과 큐 구현해보기
#도전문제
#스택과 힙 : 메모리 구조에서의 스택
#스택과 큐 : 자료구조에서의 스택

#스택 : 선입후출(First In Last Out), 후입선출 구조를 갖는 자료구조
#푸시(push): 스택에 자료를 넣는 행위
#팝(pop): 스택에서 자료를 꺼내는 행위

#스택 (선입후출 자료구조) 구현해보기
class Stack:
    def __init__(self):
        self.__list = []
    def push(self, value):
        self.__list.append(value)
    def pop(self):
        output = self.__list[-1]
        del self.__list[-1]
        return output

stack = Stack()
stack.push(10) #[10]
stack.push(20) #[10, 20]
stack.push(30) #[10, 20, 30]
print(stack.pop()) #30 [10,20]
print(stack.pop()) #20 [10]
print(stack.pop()) #10

#큐 (선입선출 자료구조) 구현해보기
class Queue:
    def __init__(self):
        self.__list = []
    def enqueue(self, value):
        self.__list.append(value)
    def dequeue(self):
        output = self.__list[0]
        del self.__list[0]
        return output
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
