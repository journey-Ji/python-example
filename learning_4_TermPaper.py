#연습문제1 : 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number%2==0:
        return True
    else:
        return False
print('\n')

#연습문제 2 : 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#연습문제 3 : 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램
'''
input1 = int(input("첫번째 숫자를 입력하세요.: "))
input2 = int(input("두번째 숫자를 입력하세요.: "))
total=0
total=input1+input2
print('두 수의 합은 %s입니다'%total)
'''

# 연습문제 4 : 다음 중 출력 결과가 다른 것 한 개를 골라 보자. --3번째 것! 1,2번은 서로 같고 4번도 띄어쓰기가 join되지 않아서 같다


print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

# 연습문제 5 : test.txt라는 파일에 Life is too short문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
f1=open("test.txt",'w')
f1.write("Life is too short")
f1.close() #파일을 닫아줘야 나중에 다시 열어줄 수 있다.
f2=open("test.txt",'r')
print(f2.read())
f2.close()

# 연습문제 6 : 사용자의 입력을 파일에 저장하는 프로그램을 작성해보자.(기존의 내용 유지해야함)
'''
user_input=input("저장할 내용을 입력하세요. :")
f=open('test1.txt','a')
f.write(user_input)
f.write("\n")
f.close()
'''

# 연습문제 7 : 다음과 같은 내용을 지닌 파일이 있을 때, 파일의 내용중 java라는 문자열을 python으로 바꿔서 저장하자
f=open('test7.txt','w')
f.write('Life is too short\nyou need java')
f=open('test7.txt','r')
body=f.read()
f.close()

body=body.replace("java","python")

f=open('test7.txt','w')
f.write(body)
f.close()

