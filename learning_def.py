#함수 공부하기
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#함수의 기본적인 생성과 사용
def add(a,b):
    return a+b
a=3
b=4
c=add(a,b)
print(c)
print('\n')

#입력값이 없는 함수
def say():
    return 'Hi'
print(say())
print('\n')

#결과값이 없는 함수
def add1(a,b):
    print('%d, %d의 합은 %d입니다.'%(a,b,a+b))
    return False
a1=add1(3,4) #여기서 함수가 실행되면서 자연스럽게 print명령어가 실행될 뿐, 실제로 결과값을 갖는건 아니다.
print(a1)
print('\n')

#매개변수 지정하여 호출하기
def add2(a,b):
    return a+b
result=add2(a=3,b=4)
print(result)
result=add2(b=5,a=1)
print(result)
print('\n')

#여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result
result=add_many(1,2,3)
print('1+2+3=',result)
result=add_many(1,2,3,4,5,6,7,8,9,10)
print('1부터10까지의 자연수 합=',result)
print('\n')

#여러개의 입력값을 처리하는 또 다른 함수
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result=result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result

result=add_mul('add',1,2,3,4,5)
print('1부터 5까지 자연수의 합 = ',result)
result=add_mul('mul',1,2,3,4,5)
print('1부터 5까지 자연수의 곱 = ',result)
print('\n')

#키워드 피라미터 공부하기 (**매개변수) 
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)
print('이처럼 **키워드 파라미터는 입력값을 딕셔너리형태인 key=value로 저장한다.')
print('\n')

#함수의 결과값은 항상 하나이다.
def add_and_mul(a,b):
    return a+b, a*b
print(add_and_mul(3,4))
print('이처럼 결과값을 하나로 묵어서 튜플 형태로 반환하게 된다.')
print('\n')

def add_and_mul2(a,b):
    return a+b
#   return a*b
print(add_and_mul2(2,3))
print('이처럼 2개의 결과값을 받고싶어서 return을 2개를 써도, 가장 처음 만난 return명령어만 수행하게 된다.')
print('\n')

#return의 또 다른 쓰임새
def say_nick(nick):
    if nick=='바보':
        return
    print('나의 별명은%s입니다'%nick)
say_nick('야호')
say_nick('바보')
print('출력된 것 처럼, 바보를 입력받으면 바로 return하여 아무것도 출력하지 않는다.')
print('\n')

#매개변수 초깃값 설정하기
def say_myself(name,old,man=True): # man=True처럼 초깃값을 설정해줄 수 있다.
    print('나의 이름은%s입니다.'%name)
    print('나이는 %s살입니다.'%old)
    if man:
        print('남자입니다')
    else:
        print('여자입니다')
say_myself("지창언",27)
say_myself("지창언",27,True)
print('이처럼 3번째 변수값을 설정해주지 않아도, 초깃값설정에 의해서 같은 결과값이 출력됨을 알 수 있다.')
say_myself('지예린',27,False)
print('\n')
#def say_myself2(name2,man=True,old): # 여기서 오류가 나는 이유 = 초깃값 설정한 매개변수는 맨 뒤에 둬야한다.
#    print('나의 이름은 %s입니다.'%name2)
#    print('나이는 %d살입니다'%old)
#    if man:
#        print('남자입니다')
#    else:
#        print('여자입니다')
#say_myself2('지창언',27)

#함수 안에서 선언한 변수의 효력 범위
a=1 # 함수 밖 변수a
def vartest(a):
    a=a+1   #함수 안 변수a
vartest(a)
print(a)
print('함수를 거쳐서 a값이 2가 출력될것 같지만, 실제로는 1이 출력된다.')
print('함수 안의 변수는 함수 안에서만 효력이 있기 때문이다. 따라서 함수 밖의 변수a가 출력된 것이다.')
print('\n')
def vartest2(test):
    test=test+1
vartest2(3)
#print(test) # 이처럼 test부분에 오류가 뜨는 것을 보면 test변수가 설정되지 않았기 때문이다.
print('\n')

#함수안에서 함수 밖의 변수를 변경하는 방법 
#1.return사용하기

a=1
def vartest_return(a):
    a=a+1
    return a
a = vartest_return(a) #함수의 결과값을 함수 밖 변수a에 대입
print(a)
print('\n')

#2.global 명령어 사용하기
a=1
def vartest_global():
    global a
    a=a+1
vartest_global()
print(a)
#하지만 global 명령어는 최대한 사용하지 않는 것이 좋다.
#함수는 독립적으로 존재해야 하기 때문이다.
print('\n')

#lambda (예약어)
#주로 def를 사용할 만큼 복잡하지 않거나, 사용할 수 없는 곳에서 사용한다.
# lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식 <<사용방법

add=lambda a,b:a+b
result=add(3,4)
print('3+4는 ',result)
print('\n')
#위 예제와 아래 예제는 완전히 동일한 예제이다
def add_lambda(a,b):
    return a+b
result=add_lambda(3,4)
print('3+4는 ',result)


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
