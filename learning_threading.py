#learning_threading.py
import time
def long_task():
    for i in range(5):
        time.sleep(0.5)
        print("working:%s\n"%i)
print("Start")
for i in range(5):
    long_task()
print("End")
#위 예제는 총 2.5*5 = 12.5초가 걸린다.

import threading

print("Start")
threads=[]
for i in range(5):
    t=threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
print("End")
#위 예제는 thread사용으로 빨라졌지만 start end 작업 순으로 간다./start 작업 end 순으로 되도록 고쳐보자


print('Start')
threads=[]
for i in range(5):
    t=threading.Thread(target=long_task) # t에 스레드 생성
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()#thread.join은 스레드가 종료될 때 까지 기다리게 한다.

print('End')