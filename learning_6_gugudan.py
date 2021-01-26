#learning_6_gugudan.py
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

def GuGu(n):
    result=[]
    i=1
    while i<10:
        result.append(n*i)
        i=i+1
    return result
print(GuGu(2))
    
#6-2
#3과 5의 배수 합하기
#10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이다. 이들의 총합은 23이다.
#1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
result=0
for n in range(1,1000):
    if n%3==0 or n%5==0:
        result=result+n

print(result)
print('\n')

#6-3
#게시판 페이징하기
#입력 : 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
#출력 : 총 페이지 수
print('게시판 페이징하기')

def getTotalPage(m,n):
    if m%n==0:#나머지가 0이면
        return m//n#나머지 반환
    else:
        return m//n+1#나머지 반환
print(getTotalPage(5,2))
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
print('\n')

#6-4 간단한 메모장 만들기
#필요한 기능 : 메모 추가, 메모 조회
#입력받는 값 : 메모 내용, 프로그램 실행 옵션
#출력하는 값 : memo.txt
print('6-4 간단한 메모장 만들기')
import sys



#6-5 탭을 4개의 공백으로 바꾸기
#필요 : 문서 파일 읽기, 문자열 변경
#입력 : 문서파일
#출력 : 수정된 문서파일
print('6-5 탭을 4개의 공백으로 바꾸기')
import sys


#6-6 하위 디렉터리 검색하기
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
