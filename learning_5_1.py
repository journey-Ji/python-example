#클래스
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

result=0
def add(num):
    global result
    result+=num
    return result
print('계산기 +3',add(3))
print('계산기 +4',add(4))
print('\n')

result1=0
result2=0

def add1(num):
    global result1
    result1+=num
    return result1
def add2(num):
    global result2
    result2+=num
    return result2

print('계산기1 +3',add1(3))
print('계산기1 +4',add1(4))
print('\n')
print('계산기2 +3',add2(3))
print('계산기2 +7',add2(7))
print('\n')
#위 처럼 계산기 함수를 여러개 만들어야 하는 경우가 있다... 너무 힘들지 ?
# 그래서 클래스를 사용한다 !

class Calculator:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result+=num
        return self.result
    def sub(self,num):
        self.result-=num
        return self.result
cal1=Calculator()
cal2=Calculator()

print('클래스 계산기1 더하기3',cal1.add(3))
print('클래스 계산기1 더하기4',cal1.add(4))
print('클래스 계산기2 더하기3',cal2.add(3))
print('클래스 계산기2 더하기7',cal2.add(7))
print('\n')

class Cookie:
    pass
a=Cookie()
b=Cookie()

class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
#메서드 호출방법 2가지
#방법1
a=FourCal()
FourCal.setdata(a,4,2)

#방법2
a=FourCal()
a.setdata(4,2)
#위 두 방법은 호출 방법에 따라 self를 넣냐 안넣냐에 차이이다.

#각 함수의 객체변수값 출력하기
print(a.first)
print(a.second)
print('\n')

a=FourCal()
b=FourCal()
a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.first)
print('\n')

print('주소값 비교')
print(id(a.first))
print(id(b.first))
print('\n')

#4+2 실행하기
print('4+2 실행하기')
a=FourCal()
a.setdata(4,2)
print('4+2 = ',a.add())
print('\n')

#4칙연산 실행하기
print('사칙연산 실행하기')
a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print('\n')


#생성자(constructor) 배우기
'''
a=FourCal()
a.add()
'''
#setdata()를 거치지 않고 위처럼 실행하면 오류가 발생한다.
#이처럼 객체에 초깃값을 설정할 필요가 있을 때에는, 초깃값을 그대로 넣는 것보다
#생성자를 구현하는 것이 안전한 방법이다.
#생성자 = 객체가 생성될 때 자동으로 호출되는 메서드
#__init__을 사용하여 생성자를 만들 수 있다.
class FourCal2():
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
#__init__으로 이름을 정하면 생성자로 인식되어, 객체가 만들어지는 시점에 자동으로 호출된다.

#a=FourCal2() 을 바로 실행하면 오류가 난다. 생성자에 first와 second를 호출해야 하는데, 값이 안정해져 있어서 그렇다.
a=FourCal2(3,4) #이렇게 first&second에 해당하는 값을 처음부터 바로 전달해주면 된다.

print(a.first)
print(a.add()) #객체변수의 값도 잘 저장되었고, 메서드도 잘 동작한다.
print('\n')

#클래스의 상속 (Inheritance)
class MoreFourCal(FourCal2):
    def pow(self):#a의 b제곱을 계산하는 함수
        result=self.first**self.second
        return result 
#위 과정을 거치면 FourCal2클래스의 모든 기능을 가진 MoreFourCal이라는 클래스를 만들게 된다.
a=MoreFourCal(4,2)
print('4+2 = ',a.add())
print('\n')
a=MoreFourCal(4,2)
print('4의 2제곱 = ',a.pow())
print('\n')

#메서드 오버라이딩
print('메서드 오버라이딩')
'''
a=FourCal2(4,0)
print(a.div())
'''
#위 명령을 실행하면 에러가 난다.4를0으로 나눌 수 없기 때문이다. 하지만 사용자가 이 때,0을 출력하도록 하고 싶다면?
class SafeFourCal(FourCal2):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a=SafeFourCal(4,0)
print(a.div())
print('\n')
#위 처럼, 같은 클래스안의 같은 메서드를 다시 쓰는 것을 메서드 오버라이딩 이라고 한다.

#나혼자코딩 : 곱하는 값이 0일 경우 'Fail'문자열을 출력하는 클래스FailFourCal을, 위에서 만든 FourCal클래스를 상속하여 만드시오
print('나혼자코딩')
class FailFourCal(FourCal2):
    def mul(self):
        if self.second==0:
            return 'Fail'
        else:
            return self.first*self.second
a=FailFourCal(4,0)
print(a.mul())
print('\n')

#클래스 변수
print('클래스 변수')
class Family:
    lastname="지"
print('\n')

a=Family()
b=Family()
print(a.lastname)
print(b.lastname)
print('\n')

print('lastname변수 변경')
Family.lastname="박"
print(Family.lastname)
print(a.lastname)
print(b.lastname)
print('\n')

print('id값 확인하기')
print('클래스 이름.변수이름 = ',id(Family.lastname))
print('a.변수이름 = ',id(a.lastname))
print('b.변수이름 = ',id(b.lastname))
#위의 id값이 같음 = 클래스 변수는 공유된다.
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
