#내장 함수
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

#abs(x) : 입력받은 수의 절댓값을 돌려주는 함수
print('abs(x)')
print(abs(4))
print(abs(-3))
print(abs(1.2))
print('\n')

#all(x) : 반복가능한 자료형을 입력받아, 하나라도 거짓이 있으면 False를 아니면 True를 반환
print('all(x)')
print(all([1,2,3]))
print(all([1,2,3,0]))
print('\n')

#any(x) : 입력값중 하나라도 참이 있으면 True, 모두 거짓이면 False를 반환 (all의 반대)
print('any(x)')
print(any([1,2,3,0]))
print('\n')

#chr(i) : 아스키(ASCII)코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
print('chr(i)')
print(chr(97))
print(chr(48))
print('\n')

#dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
print('dir')
print('리스트에 대해')
print(dir([1,2,3]))
print('\n')
print('딕셔너리에 대해')
print(dir({'1':'a'}))
print('\n')

#divmod(a,b) : 2개의 숫자릅 입력받아, a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print('divmod(7,3)')
print(divmod(7,3))
print('\n')

#enumerate : 순서가 있는 자료형을 입력받아, 안덱스값을 포함한 enumerate객체를 반환
print('enumerate()')
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
print('\n')

#eval(expression) : 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 반환
print('eval(expression)')
print(eval('1+2'))
print(eval("'hi'+' python'"))
print(eval('divmod(4,3)'))
print('\n')

#filter(함수이름,함수에 차례로 들어갈 반복 자료형) : 두번째 인수가 첫번째 인수에 입력되었을 때, 참인것만 반환
print('filter(함수이름,자료형)')
def positive(x):
    return x>0
print(list(filter(positive,[1,-3,2,0,-5,6])))
print('\n')

#hex(x) : 정수 값을 입력받아 16진수로 반환
print('hex(x)')
print(hex(234))
print(hex(3))
print('\n')

#id(object) : 입력받은 객체의 고유 주소 값을 반환
print('id(object')
a=3
print(id(3))
print(id(a))
b=a
print(id(b))
print('\n')

#input() : 사용자 입력을 받는 함수
print('input')
#a=input()
#b=input("Enter: ")
#print(a)
#print(b)
print('\n')

#int(x) : 문자열 형태의 숫자 등을 정수형태로 반환
print('int(x)')
print(int('3'))
print(int(3.4))
print('\n')

#isinstance(객체,클래스) : 입력받은 인스턴스가 클래스 내의 인스턴스인지 판단
print('isinstance')
class Person: pass
a=Person()
print(isinstance(a,Person))
b=3
print(isinstance(b,Person))
print('\n')

#len(s) : 입력값s의 길이(요소 전체 갯수)를 반환
print('len(s)')
print(len('python'))
print(len([1,2,3]))
print(len((1,'a')))
print('\n')

#list(s) : 반복자료형을 받아 리스트로 반환
print('list(s)')
print(list('python'))
print(list((1,2,3)))
print('\n')

#map(함수,반복가능자료형) : 입력받은 자료형의 요소를 함수에 넣어 수행시킨결과를 묶어서 반환
print('map(함수,반복가능자료형)')
print('map함수 사용안한 것')
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result=two_times([1,2,3,4])
print(result)
#리스트[1,2,3,4]를 입력받아서 함수(각 요소*2)를 수행시킨 후 결과값을 묶어서 리스트로 반환
print('\n')
print('map함수 사용한 것')
def two_times2(x):return x*2
print(list(map(two_times2,[1,2,3,4])))
print('\n')
#결과값 같고, 코드 줄 굉장히 많이 줄었지 ?
print('lambda이용 하면 ?')
print(list(map(lambda a: a*2,[1,2,3,4])))
print('\n')
#lambda이용을 통해 함수정의 할 필요도 없었다.

#max(반복가능자료형) : 입력받은 수들 중 최댓값을 반환
print('max(반복가능자료형)')
print(max([1,2,3]))
print(max('python'))
print('\n')

#min(반복가능자료형) : max의 반대
print('min(반복가능자료형)')
print(min([1,2,3]))
print(min('python'))
print('\n')

#oct(x) : 8진수로 반환
print('oct(x)')
print(oct(34))
print(oct(12345))
print('\n')

#open(파일이름,읽기방법) : 파일객체를 돌려주는 함수/ 읽기방법 생략시 읽기모드(r)로 반환
print('open(파일이름,읽기방법)')
try:
    f=open('binary_file','rb')#rb = 바이너리 읽기 모드
    print(f.read())
finally: f.close
print('\n')

#ord(c): 입력받은 문자의 아스키 코드 값을 돌려주는 함수
print('ord(c)')
print(ord('a'))
print(ord('0'))
print('\n')

#pow(x,y) : x의y제곱을 반환
print('pow(x,y)')
print(pow(2,4))
print(pow(3,3))
print('\n')

#range(시작숫자,끝 직전숫자) : 입력받은 숫자에 해당하는 범위값을 반복가능객체로 반환
print('인수가 하나일 때, range(x)')
print(list(range(5))) #0~4 까지
print('인수가 두개일 때, range(x,y)')
print(list(range(5,10)))#5~9 까지
print('인수가 세개일 때, range(x,y,z)')
print(list(range(1,10,2)))#1~9까지, 숫자사이의 거리=2
print(list(range(1,-10,-2)))#1~-9까지, 숫자사이의 거리 =-2
print('\n')

#round(숫자,ndigits) : 숫자를 입력받아 반올림
print('round')
print(round(4.6))#4.6반올림
print(round(4.2))#4.2반올림
print(round(5.678,2))#5.678를 소숫점2째 자리까지 반올림
print(round(5.6747,2))
print(round(5.65,2))
print('\n')

#sorted(반복가능자료형) : 입력값을 정렬하여 리스트로 반환
print('sorted(반복가능자료형)')
print(sorted([3,2,4,1]))
print(sorted(['a','c','d','f','e','b']))
print(sorted('zero'))
print(sorted((3,2,1)))
print('\n')
#리스트 자료형에도 sort()함수가 있지만 이는, 객체의 리스트를 정렬할 뿐, 돌려주지는 않는다.

#str(객체) : 문자열 형태로 객체를 반환
print('str()')
print(str(3))
print(str('hi'))
print(str('hi'.upper()))
print('\n')

#sum(반복자료형) : 입력받은 자료형의 모든요소 합을 반환
print('sum(반복자료형)')
print(sum([1,2,3,]))
print(sum((5,6,7)))
print('\n')

#tuple(반복자료형) : 반복자료형을 입력받아 튜플형태로 반환
print('tuple(반복자료형)')
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3,)))
print('\n')

#type(객체) : 입력받은 객체의 자료형을 반환
print('type(객체)')
print(type("abc"))
print(type([]))
print(type(open("test.txt",'w')))
print('\n')

#zip(*반복자료형) : 동일한 개수로 이루어진 자료형을 묶어서 반환
print('zip(*반복자료형)')
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3,],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
