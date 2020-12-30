# 숫자, 문자, 불
#리스트 튜플 딕셔너리

#변수 = 값을 담는 상자
# a=a+1 여기서의 등호는 오른쪽의 값을 왼쪽변수에 집어넣는다 의미
# a==a 이것이 평소 알고있는 등호의 의미
#정수형, 실수형, 지수표현방식, 8진수,16진수

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#정수형
a=2
print(a)
print(type(a)) # int==정수형
#실수형
b=3.14
print(b)
print(type(b))

print(a*b)
print(type(a*b))
print(1/4)
print(1//4)
aa=int(2)
bb=int(3)
print(aa/bb) #값
print(aa//bb) # 몫
print(aa%bb) # 나머지
#문자열
#문자열 자료형을 표현하는 4가지방법
cha_a = 'hellow_a'
cha_b = "hellow_b"
cha_c = '''hellow_c'''
cha_d = """hellow_d"""
print(cha_a)
print(cha_b)
print(cha_c)
print(cha_d)

big_small = """python's favorite food is perl"""
print(big_small)
print('python\'s favorite food is perl')
#위처럼 \ 백슬래시를 이용하여 문자열 작은따옴표의 사용을 컴퓨터에게 알려줄 수 있다.
print('Life is short\nYou need python')
#\n를 사용하면 엔터키효과를 낼 수 있다.
print('\t배고픈데 뭐먹지\n치킨먹자')
#\t를 사용하여 탭효과(들여쓰기)가능
print('\\이러면 백슬래시도 표현가능하지')
print('\\이러면?')
#\\백슬래시를 두번쓰면 백슬래시 표현가능하다.
#\\\\\백슬래시 뒤에 이어나오는 백슬래시는 그대로 표현된다.
print("""이거 큰 따옴표 세개 써여 문자열을 만들면

꽤나 자유롭게 표현이 가능하지
    이런거 탭이나 띄어쓰기 엔터키 마음대로 가능해""")
#"""문자열"""이렇게 세개 연달아쓰는 문자열은 \를 사용하여 줄바꾸기나 들여쓰기 안하고도
# 자유롭게 입력가능

cha_1 = "cha type"
cha_2 = "plus, let\'s do it"
print(cha_1+cha_2)
#위처럼 문자열 합치기 가능
inde_xing='123456789'
print(cha_1[0]+'= 0번째 index 표현')
print(cha_1[5]+'= 5벉재 index 표현')
print(cha_1[-1]+'= -1번째 index 표현')
print(cha_1[0:5]+'= 0~5번째 index 표현')
print(cha_1[0:3]+'= 0~3번째 index 표현')
print(cha_1[:3]+'= 3번째 index까지 표현')
print(cha_1[2:]+'= 2번째 index부터 표현')
print(inde_xing[::1]+'= 1칸 간격으로 표현')
print(inde_xing[::2]+'= 2칸 간격으로 표현')
#0이 첫 글자이며, 띄어쓰기 또한 index에 포함된다.
#-1,-2등은 역방향으로 indexing한다.
#0:4는 0~3 index까지를 의미 -->두번째 숫자의 미만자리 까지 포함
#[x:y:z]에서 마지막z자리는 간격을 의미, if 2, 2칸 간격으로 출력



#문자열 포맷팅
print('\n문\n자\n열\n포\n맷\n팅')
formating = 'fwaefwfwefwaf{age}살aweflkwjefl {name}waef'.format(name ='지창언',age=22) # {여기에 변수명1}ㅁㅈㄷㄹ{변수명2}ㅈ.format(변수명='값1',변수명='값2')
print(formating)
name='창언지'
age=24
formating=f'awelfjw{age}klawejflka{name}'#이 처럼 변수명을 밖에서 따로 지정해줄 수 도 있다.
print(formating)
ex='음 예시를 한번 들어볼까 ? \n지금 기분은? {feeling}\n지금 먹고 싶은건? {food}'.format(feeling='d',food='d')
feeling ='hungry'
food='chicken'
ex2=f'음 두번째 예시를 들어볼까 ? \n지금 기분은?{feeling}\n지금 먹고 싶은건? {food}' ### 문자열 앞에 f를 써주는것이 중요 !
print(ex)
print(ex2)

#정렬과 공백

point = "%0.2f" % 3.42134234
print(point)
munday = "%10s" %"close the door"
print(munday)
thusday = "%-10sclose" %"your eyes"
print(thusday)


# 문자 찾기, 갯수 분석
rose = "flower"
print(rose.count('f'))
print(rose.find('f'))
print(rose.find('x'))

#문자열 삽입(join)
a=",".join("abcd")
#즉 위의 콤마로 칸을 나눠서 join뒤에 있는 문자열을 삽입한다.
print(a)

#대소문자 전환
a='hi'
print(a)
a=a.upper()
print(a)
#공백없애기 strip 왜 안되니;;
a="  hi Hi  d"

a.strip()

#문자열 바꾸기
a='life is too short'
print(a.replace('life', 'time of goodness'))

#리스트
a=['이시영','지창언','성정희','지병규','지예린','지예원','한효주']
print(a)
print(a[1])
print(a[0])
print(a)
a[0:2] =['change','change']
print(a)
a[0:2]=[]
print(a)
print(a[0])

print(a[4])

#리스트에 추가하기. append
a.append('추가1')
print(a)
#리스트 정렬하기 sort
a.sort()
print(a)
#리스트 뒤집기 reverse
a.reverse()
print(a)

#위치반환 index
print(a.index('지병규'))

#index 특정자리에 삽입
a=[1,5,3]
a.insert(0,4)
print(a)

#제거하기 remove(삭제할 값) 주의! 변수가 index가 아닌 값이다.
a=[1,5,3,1,1,1,1]
a.remove(1)
print(a)

#pop() 인덱스의 마지막 자리에 있는 값이 출력된다.
a=[1,2,3,4,5]
print(a.pop())
print(a)

#count() 리스트에 있는 값의 개수를 세어줌
print(a.count(1))

#extend() 리스트에 리스트를 넣어준다.
a=[1,3,5,7,9]
a.extend([2,4,6,8])
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')