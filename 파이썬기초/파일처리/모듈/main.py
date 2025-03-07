import hellomodule
# print(hellomodule.a)
# print(hellomodule.b)
# print(hellomodule.C)
print(hellomodule.Circle(10))

from hellomodule import Circle
# print(Circle().넓이(5)) #안됨
print(Circle(5).둘레()) #됨

print("#main")
print(__name__) #__main__ #메인아닐경우 __없음

# if __name__ == __main__ 조건문

if __name__ =="__main__":
    print("##넓이()검증시작")
    if Circle(10).넓이() - 314 < 10**7:
        print("넓이 검증 성공!:Success")
    else : print("넓이가 다릅니다: Fail")
    Circle(10).둘레() == 356
#이 파일이 메인으로 실행되었는지에 대한 조건문임.
