    #조건문, boolean자료형
 #불 자료형 - True, False 두가지 형태(첫 대문자 필수)
 #어떠한 '명제'의 결과를 True와 False로 구분
 #비교연산자(부등호)로 활용. ==:비교연산자, =:할당연산자. 구분하기
 ## 단항 not
 ## 불연산자를 반대값으로 만듦.
#  not True # False
#  not False # Ture
    #and, or
     #and=둘다 True일때만 True
     #or = 둘중 하나라도 True 일때 True

#날짜/시간 구하기
import datetime
import pytz
seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)
print(f"년도={now.year}, 월={now.month}, 일={now.day}")