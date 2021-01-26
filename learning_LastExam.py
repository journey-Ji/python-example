# Q1 : 문자열 바꾸기
#a:b:c:d를 a#b#c#d#으로 바꾸시오
print('Q1')
a='a:b:c:d'
a=a.split(':')
print(a)
b="#".join(a)
print(b)
print('\n')

# Q2 : 딕셔너리 값 추출하기
print('Q2')
a={'A':90,'B':80}
try:
    print(a['C'])
except KeyError:
    print('70')
print('\n')

# Q3
print('Q3')
a=[1,2,3]
a+=[4,5]
print(a)
b=[1,2,3]
b.extend([4,5])
print(b)
print('리스트 요소 추가시 +기호나 extend함수는 같은 역할을 한다.')
print('\n')

# Q4
print('Q4')
A=[20,55,67,82,45,33,90,87,100,25]
total=0
numbers=0
for i in A:
    if i>50:
        total+=i
        numbers+=1
print('총점 : ',total)
print(numbers)
print('평균 : ',total/numbers)
print('\n')

# Q5 : 피보나치 함수
print('Q5')
a=input('정수를 입력하세요')
a=int(a)
b=a
c=a+b           #a1 b1 c1 a2 b2 c2 a3 b3 c3
while a<999:
    print(a,end=' ')
    print(b,end=' ')
    print(c,end=' ')
    a= b+c
    b= c+a
    c= a+b

print('\n')

# Q6 : 숫자의 총합 구하기 / 숫자를 입력받고 그 총합을 구하기
print('Q6')
numbers=input("숫자들을 입력하시오")
numbers=numbers.split(',')
print(numbers)
total=0
for i in range(len(numbers)):
    point=numbers[i]
    total=total+int(point)
print('총합은 : ',total,'입니다.')
print('\n')

# Q7 : 2~9의 숫자를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성
print('Q7')
number=0
number=input("2~9 사이의 숫자를 입력해 주세요")
number=int(number)
if number>9 and number<2:
    number=input("2~9 사이의 숫자를 입력해 주세요")
    number=int(number)
i=1
while i<10:
    print(number*i,end=' ')
    i=i+1
print('\n')

# Q8 : 파일의 내용을 역순으로 배열하여 저장하시오

print('Q8')
f=open('abc.txt','r')
lines=f.readlines()
f.close()
lines.reverse() #역순 정렬
f=open('abc.txt','w')
for line in lines:
    line=line.strip() # 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')
f.close()
print('\n')

# Q3
print('Q2')
print('\n')

# 10
print('10')
class Calculator:
    
    def __init__(self,numberList):
        self.numberList=numberList
    def add(self):
        result=0
        for num in self.numberList:
            result+=num
        return result
    def avg(self):
        total=self.add
        return total/len(self.numberList)


print('\n')

