import mod1

#모듈 배우기
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#모듈 만들기
print('모듈사용1')
print('3+4 = ',mod1.add(3,4))
print('4-2 = ',mod1.sub(4,2))
print('\n')
#위 처럼 모듈에 존재하는 함수들을 사용할 수 있다.

#모듈 이름을 붙이지 않고, 모듈 내 함수를 바로 사용하는 방법
print('모듈사용2')
from mod1 import add
print('3+4 = ',add(3,4))
print('\n')

#모듈 내 함수를 바로, 여러개 사용하는 방법1
print('모듈사용3')
from mod1 import add,sub
print('3+4 = ',add(3,4))
print('4-2 = ',sub(4,2))
print('\n')

#모듈 내 함수를 바로, 여러개 사용하는 방법2
print('모듈사용4')
from mod1 import * #mo1모듈 내의 모든 함수를 사용가능 (*)별표 = 모두
print('3+4 = ',add(3,4))
print('4-2 = ',sub(4,2))
print('\n')


#if __name__ =="__main__": 의 의미

#클래스나 변수 등을 포함한 모듈
print('클래스나 변수 등을 포함한 모듈')
import mod2 #모듈 불러오기
print('파이 값은 = ',mod2.PI)
a=mod2.Math()
print('반지름이2인 원의 넓이 = ',a.solv(2))
print('파이+4.4 = ',mod2.add(mod2.PI,4.4))
print('\n')
#위 처럼 모듈내에 저장되어 있는 변수 값과 클래스들을 사용할 수 있다.

#나 혼자 코딩 : mod2.py모듈을 사용해 반지름이 5인 원의 넓이를 계산해 보자.
print('나 혼자 코딩')
a=mod2.Math() #모듈 내 클래스 불러오기
print('반지름이5인 원의 넓이=',a.solv(5)) #클래스 내의 함수 사용
print('\n')

#다른 파일에서 모듈 불러오기
#modtest.py 파일 참고

#모듈을 불러오는 또 다른 방법1
print('모듈을 불러오는 또 다른 방법')
import sys
print(sys.path) #sys.path에 파이썬 모듈이 들어있다면, 모듈이 저장된 디렉토리로 이동할 필요 없이 사용가능하다
# 그러니까 우리는 sys.path에 우리가 만든 mod2.py가 들어있는 디렉토리를 저장해 줄 것이다.
sys.path.append('/Users/jizone/Desktop/codingJone/mymod')
print(sys.path)
#위 과정을 통해 Path에 해당 디렉토리의 등록이 확인되면, import가 가능하다 !

#모듈을 불러오는 또 다른 방법2
print('모듈을 불러오는 또 다른 방법2')
#set PYTHONPATH=/Users/jizone/Desktop/codingJone/mymod
#위 명령어를 입력하면 PYTHONPATH 환경변수에 mymod의 디렉토리가 저장되면서
#이 후에, import가 가능해진다.





print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
