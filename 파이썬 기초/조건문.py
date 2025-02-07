#if조건문
#-들여쓰기 중요(tab키로)
 ## 조건이 True일때만 들여쓰기 안쪽의 문장을 실행한다.
# if True:
#     print("True입니다!")#결과o
# if False:
#     print("False입니다")#결과x

# raw_input = input("정수를입력해주세요: ")
# raw_input = int(raw_input)

import datetime
import pytz
seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)
# print(f"년도={now.year}, 월={now.month}, 일={now.day}")
# m = now.month

 # 조건문
#  if 조건: 복합 문장
# 복합 문장 : 문장을 묶어 놓은 것
#들여쓰기 잘못했을 경우 :: Indent 에러 나옴

## 홀수짝수 조건문
raw = input("정수입력:")
l = int(raw[-1])
if l%2 == 1:
    print("홀수")
else: print("짝수")

# ## if else와 elif 구분
# # elif : if조건 뒤에있는 조건문을 표현. 다음조건에 대한 표현? 이랄까
# if :
#     print("a")
# elif : #들여쓰기 if문과 동일
#     print("b")
# else : #들여쓰기 if문과 동일
#     print("c")
#  #if문 여러개쓰는것에 비해 코드 단계가 감소함. (경제적)

#자료형 변환
int()
float()
str()
bool() #None, 숫자0, 빈컨테이너, 빈 문자열 등=0

# ##pass구문
# if문 뒤에 Suite()#복합구문
# 없을때 pass를 통해 나중에 작성할 수 있도록 함. 
# ex)
# if i :
#     pass #raise Not ImplementedError로 대체 가능.
#       raise는 오류 발생시킴. 개발전인 부분 알수있게 해줌
# else:
#     print("프로그램을 다시실행하세요")
