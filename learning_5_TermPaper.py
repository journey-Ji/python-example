# 연습문제 1 : calculator 클래스에 minus메서드를 추가해 보자.
class Calculator:
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value+=val
print('연습문제 1')
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value-=val

cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
print('\n')

# 연습문제 2 : 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator클래스를 만들어보자.
print('연습문제 2')
class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value=0
        if self.value>100:
            self.value=100
        else: pass
    def add(self,val):
        self.value+=val
        if self.value>100:
            self.value=100
        else: pass


cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#연습문제 3 : 다음 결과를 예측해 보자
print('연습문제 3')
print(all([1,2,abs(-3)-3])) #False값이 나온다 / abs=절댓값
print(chr(ord('a'))=='a') #True값이 나온다 / ord = 유니코드화 chr = 유니코드를 문자열로
print('\n')

#연습문제 4 : filter와 lambda 사용하여 리스트[1,-2,3,-5,8,-3]에서 음수를 모두 제거해 보자.
print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))

#연습문제 5 : 0xea라는 16진수 문자열을 10진수로 변경해보자
print(int('0xea',16))

#연습문제 6 : map과 lambda를 사용하여 [1,2,3,4]에 각3이 곱해진 리스트를 만들자 

print(list(map(lambda a: a*3,[1,2,3,4])))

#연습문제 7 : 다음 리스트의 최댓값과 최솟값의 합을 구해보자.
print('연습문제 7')
a=[-8,2,7,5,-3,5,0,1]
print(max(a))
print(min(a))
print('\n')

#연습문제 8 : 17/3의 결과를 소숫점4자리까지만 반올림하여 표시해 보자.
print('연습문제 8')
print(round(17/3,4))
print('\n')

####연습문제 9 : 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해보자.
'''#myargv.py
import sys
numbers=sys.argv[1:]
result=0
for number in numbers:
    result+=int(number)
print(result)
'''

#연습문제 10 : os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
#1. /Users/jizone/Desktop/codingJone 디렉터리로 이동한다.
#2. dir명령을 실행하고 그 결과를 변수에 담는다.
#3. dir 명령의 결과를 출력한다.

#연습분제 11 : glob 모듈을 사용하여 Users/jizone/Desktop/codingJone 디렉터리의 파일 중 확장자가
#.py인 파일만 출력하는 프로그램을 작성해 보자.
print('연습문제 11')
import glob
print(glob.glob("Users/jizone/Desktop/codingJone/*.py"))
print('\n')

#연습문제 12 : time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
#2018/04/03 17:20:32
import time
print('연습문제 12')
print(time.strftime("%Y/%m/%d %H:%M:%S"))
print('\n')

#연습문제 13 : random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(중복된 숫자x)
print('연습문제 13')
import random
result=[]
while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)
print('\n')