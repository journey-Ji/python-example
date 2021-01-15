#연습문제1 홍길동씨의 평균점수 구하기

lang=80
eng=75
mat=55
total= lang+eng+mat
avg=total/3
print(total)
print(avg)
print('\n')

#연습문제2 13이 홀수인지 짝수인지 판별해보자.
num=13
나머지=num%2
print(나머지)
if 나머지==1:
    print('홀수')
else:
    print('짝수')
print('\n')

#연습문제 881120-1068234를 생년월일과 뒷부분을 나눠서 출력해보자
pin="881120-1068234"
yymmdd=pin[0:6]
num=pin[7:14]
print(yymmdd)
print(num)
print('\n')


#연습문제4번 : 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
pin="881120-1069234"
print(pin[7])
print('\n')

#물자열의 replace함수를 이용하여 :를 #으로 바꿔라
a="a:b:c:d"
print(a)
b=a.replace(':','#')
print(b)
print('\n')

#연습문제6 : [1,3,5,4,2]리스트를 [5,4,3,2,1]로 만들자
a=[1,3,5,4,2]
a.sort(reverse=1)
print(a)

#연습문제7 : ['life','is','too','shor']리스트를 life is too short문자열로 만들어 출력해보자
a=['Life','is','too','short']
result=' '.join(a)
print(a,'join함수를 사용하여 문자열 출력')
print(result)
print('\n')

#연습문제8번 : (1,2,3) 튜플값에 4를 추가하여 (1,2,3,4)를 만들어보자
#공부하기
a=(1,2,3)
a=a+(4,)
print(a)
print('\n')
##이상하네 ? 튜플은 값을 변경하거나 삭제할 수만 없고 추가는 가능하다는 말인가?
#+(값,)이런식으로 추가하면 추가가 되는데 ?


#연습문제 9 : 오류가 발생하는 상황을 고르고 바꿀 수 있으면 바꿔라
a=dict()
print(a)
a['name']='python'
a[('a',)]='python' # 튜플인 key로 사용가능하다. 
#a[[1]]='python' # list는 key로 쓸 수 없다.
#key로 쓸 수 있느냐 없느냐는 그 값이 바뀔 수 있느냐 없느냐 이다.
a[250]='python'
print('\n')

#연습문제 10 : 딕셔너리a에서 B에 해당되는 값을 추출하자.
a={'A':90,'B':80,'C':70}
result=a.pop('B') # pop함수를 이용하여 key가 'B'에 해당하는 것을 추출함
print(a)
print(result)
print('\n')

#연습문제 11 : a리스트에서 중복숫자를 제거해 보자.
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a) # 집합자료형인 set()은 요솟값이 중복될 수 없다.
b=list(aSet)
print(b)
print('\n')

#연습문제 12 다음과 같이 나오는 이유에 대해 설명하라
a=b=[1,2,3]
a[1]=4
print(a)
print(b)
print('a=b=[1,2,3]을 하면 두 변수가 같은 주소값을 가지기 때문에, 한 쪽의 값을 변경하면 다른 쪽도 같이 변경된다.')
print('\n')

