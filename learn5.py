#多线程
import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
    time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target= loop, name= 'LoopThread')
t.start()
t.join()
print('threa %s ended' % threading.current_thread().name)


lock = threading.Lock()
#获取锁
# lock.acquare()
#用完释放
#lock.release()

balance = 0
def runThread(n):
    for i in range(n):
        lock.acquare()
        try:
            balance = balance + 5
            balance = balance - 5
        finally:
            lock.release()


#threadLocal
#解决了每个线程中局部变量在函数调用中传来传去的问题

#创建threadlocal对象
local_school = threading.local()

def process_student():
    #获取当前线程的student
    std = local_school.student
    print('hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread,args= ('alice',),name = 'Thread-A')
t2 = threading.Thread(target= process_thread,args=('bob',),name = 'thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

#对应到Python语言，单线程的异步编程模型称为协程，
# 有了协程的支持，就可以基于事件驱动编写高效的多任务程序。


