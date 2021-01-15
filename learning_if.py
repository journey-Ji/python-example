print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
money=True
if money:
    print('택시를 타자')
else:
    print('걸어 가자')
print('\n')

money=2000
card=True
if money>=3000 or card:
    print('택시를 타자')
else:
    print('걸어 가자')
print('\n')


print('1이 [1,2,3]안에 있는가?',1 in [1,2,3])
print('1이 [1,2,3]안에 없는가?',1 not in [1,2,3])

print('a' in('a','b','c'))
print('j' not in 'python')

pocket=['paper','cellphone','money']
if 'money' in pocket:
    print('돈이 있으니 택시를 타자')
else:
    print('돈이 없으니 걸어 가자')

if 'card' in pocket:
    print('카드가 있으니 버스를 타자')
else:
    print('카드가 없으니 걸어 가자')

#elif사용하기

if 'card' in pocket:
    print('버스를 타자')
elif 'money' in pocket:
    print('택시를 타자')
else:
    print('걸어 가자')

if 'money' in pocket:pass
else:
    print('카드를 꺼내자')

#조건부 표현식 // 조건문이 참일 때 명령 if 조건문 else 조건문이 거짓일 때 명령
score=30
message='success' if score>=60 else 'failure'
print(message)



print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
