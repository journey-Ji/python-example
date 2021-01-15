# 자료형 2번째 수업
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print("""튜플과 리스트의 가장 큰 차이 = 값을 변화시킬 수 있는가 없는가""")
#리스느는 [] 대괄호를 사용 //만들어진 이후에도 추가, 수정 가능
#튜플 ()소괄호를 사용 // 만들어진 이후에 추가, 수정 불가
t1= (1,2,'a','b')

print('당연히 슬라이싱 등은 된다. 개체에 변화를 주는 것이 아니니까')
print(t1[0:2]) 

t2=(3,4)
print(t1+t2)
t3=t1+t2
print(t3)
print(t3*3)

a=(1,2)
a=a*3
#여기서 튜플(1,2)는 s라는 변수에 저장되어 있고,
#이 튜플(1,2)자체는 변하지 않은 채로 3번곱해져 다시 a에 저장되는 원리이다.



print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ딕셔너리ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

dic ={'name':'창언','age':26}
print(dic['name'])
print(dic['age'])
a={1:'a'}
print(a)
a['name']= "익명"
print(a)
del a[1]
print(a)
a={1:'a',1:'b'}
print('같은 키인 1을 두 개 저장했더니 뒤에있는 1의 값인 b만 나온다')
print(a) # 즉, 키가 중복되면 안되고, 만약중복되면 마지막에 나온 키를 가져온다.

print(dic['name'])

a={'name': 'jone','phone':'01042225963','birth':'1210'}
print('a딕셔너리의 keys만 뽑아서 출력하는 명령어 a.keys()')
print(a.keys())


#딕셔너리는 key 와 value로 이루어져 있다.
#삭제 추가 첨가는 key를 통해 진행한다.

b={1:'순대국밥',2:'지창언',3:'27세'}
print('b딕의 키들을 같이 출력하기 {}'.format(list(b.keys())))
#list(a.keys()) 명령어는 a의 keys을 리스트에 삽입하여 출력한다.
print(b.keys()) #b.keys()키들만 가져오는 명령어
print(b.values()) #b.values() 값들만 가져오는 명령어
print(b.items()) #b.items() 키와 값을 묶어서 같이 반환함
for k in b.keys():
    print(k)
for v in b.values():
    print(v)
for k,v in b.items():
    print("키는:"+str(k))
    print("값은:"+v)
#print(b.[4]) # 키값이 없으면 바로 구문에러가 난다.
print(b.get(4)) # 키가 없어도 none 문자열을 반환하여 구문에러는 나지 않는다.
print(b.get(4,'없음')) #이렇게 없었을 때의 반환값도 지정해줄 수 있다.

print('name'in b)
print(1 in b)
print(b.get(1))
b.clear() # 딕셔너리 비우기
print(b)

#나혼자 코딩
dic_alone={'name':'홍길동','birth':'1128','age':28}
print(dic_alone)



print('--------------------------집합자료형------------------------------')
print('--------------------------집합자료형------------------------------')
s1= set([1,2,3])
print(s1)

s2=set("hello")
print(s2)
print('set()자료형은 중복을 허용하지 않으며, 순서가 없다. 즉, 인덱싱할 수 없다.')
# 그러면 set()자료형을 indexing하려면 ? -->list화 한 후에 indexing한다(딕셔너리도 마찬가지)
print('list자료형에 set()자료형 삽입')
li=list(s1)
print(li)
print(li[0])

print('tuple자료형에 set()자료형 삽입')
t1=tuple(s1)
print(t1)
print(t1[0])

#그러면 이 set 자료형을 어떻게 유용하게 쓸까?
# set 자료형 사용처 : 교집합, 합집합, 차집합을 구할 때,
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print('&기호를 이용(교집합)')
print(s1&s2) # &기호가 교집합기호(and연산)
print('s1.intersection(s2)를 이용')
print(s1.intersection(s2))# 같은 결과값을 출력
print('\n')

print('|기호(엔터키 위에)를 이용하여 합집합')
print(s1|s2)
print('s1.union(s2)를 이용하여 합집합')
print(s1.union(s2))
print('4,5,6처럼 중복값은 한번씩만 표현된다.')
print('\n')

print('-키를 이용하여 차집합')
print(s1-s2)
print('s1.difference(s2)를 이용하여 차집합')
print(s1.difference(s2))
print('\n')

print('s1.add이용하여 자료형에 값 추가하기')
s1=set([1,2,3,])
s1.add(4)
print(s1)
print('\n')

print('s1.update([4,5,6])이용하여 한번에 여러개의 값 추가하기')
s1.update([5,6,7])
print(s1)
print('\n')

print('s1.remove(값)를 이용하여 특정값 제거하기')
s1.remove(2)
print(s1)
print('\n')

print('bool자료형 = 참/거짓판정')
a=str
b=bool
a=True
b=False

print(type(a))
print(type(b))
print('1=1 인가 ?',1==1)
print('2보다 1이 큰가?',2>1)
print('1보다 2가 큰가?',1>2)
print('\n')

a=[1,2,3,4]
while a:
    print(a.pop())
print('\n')

if []:
    print('참')
else:
    print('거짓')
print('\n')

if[1,2,3]:
    print('참')
else:
    print('거짓')
print('\n')

print('값이 있는 문자열의 bool값=',bool('python'))
print('\n')
print('빈문자열의 bool값=',bool(''))
print('\n')

a=[1,2,3]
print('a변수의 주소 값',id(a))
b=a
print('b변수의 주소 값',id(b))
print('즉 b=a라는 명령어는 a의 주소값을 b도 참조하는 것이라고 할 수 있다.')
print('\n')

print('변수의 값만 가져오면서 다른 주소를 지정하는 방법 첫번째!!b=a[:]')
a=[1,2,3]
b=a[:]
a[1]=4
print('a의 변수값',a)
print('b의 변수값',b)
print('\n')

print('변수의 값만 가져오면서 다른 주소를 지정하는 방법 두번째!!copy모듈 사용')
from copy import copy
a=[1,2,3]
b=copy(a)
print('a의 값을 출력',a)
print('b의 값을 출력',b)
print('a와 b의 주소가 같은가 ?',b is a)
print('\n')

print('변수를 만드는 여러가지 방법')
#튜플 만들기
a,b=('python','life')
(a1,b1)='python','life'
#위 두개는 완전 동일한 명령어이다. (튜플은 괄호를 생략가능)

#리스트 만들기
[a,b]=['python','life']

#여러개의 변수에 같은 값을 대입하기
a=b='python'
print('한번에 여러개의 변수에 값을 대입하면 그 주소값은 같다?',a is b)

#각 변수의 값 바꾸기
a=3
b=5
print(a,'and',b)
print(id(a),'and',id(b))

a,b=b,a
print(a,'and',b)
print(id(a),'and',id(b))

print('즉 a,b=b,a라는 명령어는 값을 바꾸는 것이 아닌 주소값을 바꾸는 것이다.')
print('\n')
