#mod1-2.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
if __name__=="__main__": #이 모듈 파일을 직접실행 했을 때 =True /다른 파일에서 모듈을 불러서 사용할 때 = False
    print(add(1,4))
    print(sub(4,2))
#즉, 위의 if__name__=="__main__": 이 처리를 해주어야 무조건적으로 print명령어가 나가는 것을 방지해준다.

# __name__ 변수는 파일을 직접 실행할 경우 __main__값이 저장된다.
# 파이썬 셸이나 다른 모듈에서 import 할 경우에는 모듈이름 값인 mod1-2가 저장된다