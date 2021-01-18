#for문 배우기
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

#리스트의 마지막 요소까지 for문을 진행한다.
test_list=['one','two','three']
for i in test_list:
    print(i)
print('\n')

#튜플을 사용하는 for문
a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
print('\n')

marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number +1
    if mark>=60:
        print('%d번 학생은 합격입니다.'%number)

    else:
        print('%d번 학생은 불합격입니다.'%number)
print('\n')

#for문의 continue사용하기
number=0
for mark in marks:
    number=number+1
    if mark<60:continue
    print('%d번 학생 축하합니다. 합격입니다'%number)

#for문의 range함수 사용하기

a=range(10)
print(a,' = 0부터 10미만의 수를 포함하는 객체이다')

#range함수 이용하여서 1부터 10까지의 수 더하기
add=0
for i in range(1,11):
    add=add+i
print(add)

#60점이상이면 합격을 출력하는 예제를 range이용하기
for number in range(len(marks)):
    if marks[number]<60: continue
    print('%d번 학생 축하합니다. 합격입니다.'%(number+1))

#for와 range이용하여 구구단 만들기

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')
print('\n')

for i in range(1,10):
    for j in range(2,10):
        print(i*j, end=' ')
    print('')
    
#리스트 내포(list comprehesion)사용안하면 ?
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)
print('\n')
#리스트 내포 사용하면 ?
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)
# 이렇게 확 간단해짐

a=[1,2,3,4]
result=[num*3 for num in a if num%2==0] # 짝수에만 2를 곱해서 출력
print(result)
print('\n')

#구구단의 모든 결과를 리스트에 담기 // 내포 사용
result=[x*y for x in range(2,10)
    for y in range(1,10)]
print(result)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ종료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
