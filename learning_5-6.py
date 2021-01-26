#5-6외장 함수

#pickle : 객체의 형태를 유지하면서 파일에 저장하고 불러오는 모듈/어떤 자료형이든 저장,불러오기 가능
import pickle
f=open("test.txt",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f) # data변수를 파일에 저장 -dump함수
f.close()
f=open("test.txt",'rb')
data=pickle.load(f) #파일에 저장된 값을 data변수로 불러옴 
print(data)
print('\n')


#os : 환경변수, 디렉터리, 파일등의 os자원을 제어하는 모듈
#내 시스템의 환경변수 값을 알고 싶을 때 : os.environ
import os
print(os.environ)
print('\n')
print(os.environ['PATH'])

#os.chdir : 디렉터리 위치 변경
#os.getcwd : 디렉터리 위치 돌려받기
#os.system : 시스템 명령어 호출
#os.popen : 실행한 시스템 명령어의 결과값 돌려받기
#os.mkdir : 디렉터리 생성
#os.rmdir : 디렉터리 삭제
#os.unlink : 파일 지우기
#os.rename(src,dst) : src라는 파일의 이름을 dst로 변경

#shutil : 파일을 복사해주는 모듈
'''
import shutil
shutil.copy("src.txt","dst.txt")
print('\n')
'''

#glob : 디렉터리에 존재하는 파일이름 불러오기
import glob
print(glob.glob("/Users/jizone/Desktop/codingJone/learning*"))#leaning으로 시작하는 파일을 모두 찾아서 읽어들임
print('\n')

#tempfile : 파일을 임시로 만들어 사용
import tempfile
filename=tempfile.mktemp() #무작위 이름의 임시파일을 만들어 돌려준다.
print(filename)
print('\n')
f=tempfile.TemporaryFile()#기본적으로 바이너리쓰기모드(wb)인 임시 저장공간 용 파일 객체를 돌려준다.
f.close()

#time : 시간과 관련된 모듈
import time
print(time.time())# time.time()은 1970.01.01/0시0분0초를 기준으로 지난 시간을 초 단위로 돌려준다.
print(time.localtime(time.time()))#time.time()의 반환값을 이용하여, 연 월 일 시 분 초 단위로 바꿔준다.
print(time.asctime(time.localtime(time.time())))#보기 쉬운 형태로 반환한다.
print(time.ctime())#아주 간편하게 출력가능,but 현재 시간만 가능

for i in range(10):
    print(i)
    time.sleep(0.1)#일정한 시간 간격을 두고 루프를 실행할 수 있다.

#calendar : 달력을 볼 수 있게 해주는 모듈
import calendar
print(calendar.calendar(2015)) #2015년도의 전체 달력 확인 가능
#위 print문은 calendar.prcal(2015)와 완전히 똑같은 결과값을 반환
print(calendar.weekday(2021,1,22))#해당 날짜의 요일을 정수로 반환 0123456=월화수목금토일
print(calendar.monthrange(2021,1))#해당 연월에 1일이 무슨요일인지, 며칠까지 있는지 보여줌
print('\n')

#random함수 : 난수를 발생시키는 모듈
import random
print(random.random())#0.0~1.0사이의 실수 중 난수
print(random.randint(1,10))#1~10 사이의 정수 중 난수
print(random.randint(1,55))#1~55 사이의 정수 중 난수
print('\n')

def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)
if __name__=="__main__":
    data=[1,2,3,4,5]
    while data: print(random_pop(data))

def random_pop2(data):
    number=random.choice(data)
    data.remove(number)
    return number

#random.shuffle
data=[1,2,3,4,5]
random.shuffle(data) #리스트의 항목을 무작위로 섞는다.
print(data)
print('\n')

#webbrowser : 기본 웹 브라우저를 실행시키는 모듈
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")



