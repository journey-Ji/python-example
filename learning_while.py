#while문 
print('----------------시작------------------')

treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print('나무를 %d번 찍었습니다'%treeHit)
    if treeHit==10:
        print('나무가 넘어갑니다.')
print('\n')

#숫자를 입력받아 해당 숫자에서 while문을 종료하기
prompt="""
1.Add
2.Del
3.List
4.Quit
Enter number: """
number=0
#while number !=4:
#    print(prompt)
#    number=int(input())
print('\n')

#while문을 강제로 빠져나가기
coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee=coffee-1
    print('남은 커피의 양은 %d개입니다.'%coffee)
    if coffee==0:
        break
print('\n')

#while문의 처음으로 돌아가기 continue
a=0
while a<10:
    a=a+1
    if a%2==0: continue
    print(a)
print('\n')

#while문의 무한루프 빠져나가기.
#while True:
#    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")



print('------------------종료-----------------')

