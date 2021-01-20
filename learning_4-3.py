import sys
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
'''
f=open("새파일.txt",'w')
f.close()
'''

#파일을 쓰기모드로 열어 출력값 적기
'''
f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
'''

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

#방법1 readline함수 사용하기
f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'r')
line=f.readline()
print(line)
f.close()
print('\n')

f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'r')
while True:
    line=f.readline()
    if not line:break  #readline()은 더 이상 읽을 줄이 없으면 None을 반환한다.
    print(line)
f.close()
print('\n')

#readlines 함수 사용하기
print('readlines 함수 사용하기')
f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()
print('\n')

#read 함수 사용하기 : 파일의 내용 전체를 문자열로 돌려준다.
print('read 함수 사용하기')
f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'r')
data=f.read()
print(data)
f.close()
print('\n')

##파일에 새로운 내용 추가하기 : 쓰기모드(w)로 파일을 열면 기존에 존재하던 내용이 사라진다.
## 기존에 존재하던 내용을 유지한채, 내용을 추가하려면 추가모드(a)를 이용하자!

f=open("/Users/jizone/Desktop/codingJone/새파일2.txt",'a')
for i in range(11,20):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
print('\n')

#with문과 함께 사용하기 close()를 항상해주는 것이 좋은데, 이를 자동화하고 싶을 때,
with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python")
print('이처럼 with문을 사용하면, with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.')
print('\n')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
