#5-4 예외 처리 : try, except등을 통해 예외적으로 오류를 넘어갈 수 있게 해줌
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

#오류 종류 1 : 디렉터리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류
'''f=open("나 없는 파일",'r')'''
#이대로 실행하면 당연히 없는파일이라 안열린다.

#오류 종류 2 : 잘못된 연산
'''print(4/0)'''
#0으로 다른 숫자를 나누는 경우 당연히 에러 발생

#오류 종류 3 :  리스트 내에서 얻을 수 없는 값
'''
a=[1,2,3]
print(a[4])
'''

#오류 예외 처리 기법 1-1 : try except문 : try블록 수행 중 오류가 발생하면 except블록이 수행된다.
'''
try:
    print(4/0)
except:
'''
#오류 종류와 상관없이 발생하면 바로except블록을 수행

#오류 예외 처리 기법 1-2 : 발생 오류만 포함한except
'''
try:
    print(4/0)
except ZeroDivisionError:
#ZeroDivisionError 발생시에만 except블록 수행
'''
#오류 예외 처리 기법 1-3 : 발생오류+오류 메시지 변수까지 포함
try:
    print(4/0)
except ZeroDivisionError as e:
    print(e)
print('\n')

#나 혼자 코딩 : 앞에서 나온 3번 방법을 사용해 IndexError가 발생할 때 오류 메시지를 출력하는 소스를 작성
try:
    a=[1,2,3]
    print(a[4])
except IndexError as i:
    print(i)
print('\n')

#오류 예외 처리 기법 2 : try -finally : finally 절은 try문 수행 도중 예외 발생 여부와 상관없이 수행
#주로 사용한 리소스를 close해야 할 때 많이 사용
f=open('foo.txt','w')
try:
    #무언가를 수행한다.
    f.write('hihi')
finally:
    f.close()
print('\n')

#오류 예외 처리 기법 3 : 여러 개의 오류 처리하기
try:
    a=[1,2]
    print(a[3])
    print(4/0)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱할 수 없습니다.')
print('\n')
#indexing오류가 먼저 발생하였으므로, 4/0에 대한 오류는 발생하지 않는다.


#오류 회피하기
try:
    f=open("나 없는 파일",'r')
except FileNotFoundError: #파일이 없으면 
    pass                    #오류를 일으키지 않고 바로 패스 시킨다.

#오류 일부러 발생시키기 : raise(오류 강제 발생)

class Bird:
    def fly(self):
        raise NotImplementedError
'''
class Eagle(Bird):
    pass
eagle =Eagle()
eagle.fly()
'''
#위에서 Bird클래스를 상속받은 Eagle클래스가 fly 함수를 설정해주지 않았기 때문에, fly를 사용하면 오류가 난다.

class Eagle(Bird):
    def fly(self):
        print('very fast')

eagle=Eagle()
eagle.fly()
print('\n')
#위 처럼, fly함수를 설정해주면 오류가 나지 않는다.

#예외 만들기 :Exceiption클래스의 상속
class MyError(Exception):
    def __str__(self): #__str__메서드는 print(e)처럼 오류메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
        return '허용되지 않는 별명입니다.'

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)
say_nick('천사')
#say_nick('바보')
print('\n')

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않는 별명입니다.')
print('\n')
#위 처럼 try except를 사용하여 만들어둔 예외로 예외처리 가능

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
