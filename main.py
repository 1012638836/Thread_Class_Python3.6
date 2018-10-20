'''多线程类的实现'''
import threading
from time import sleep,ctime
'''
    这里MyThread继承自Thread类，我们重写了它的构造函数与run方法。
    当thread类的对象调用start()方法时，会自动调用MyThread类的run()方法
    run()方法将参数args传递给super_play()方法
'''
class MyThread(threading.Thread):
    '''构造方法'''
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)

def super_play(file,time):
    for i in range(2):
        print('Start playing: %s! %s'%(file,ctime()))
        sleep(time)

list = {'曲目1.mp3':3,'曲目2.mp3':5}

threads = []
files = range(len(list))

for k,v in list.items():
    t = MyThread(super_play,(k,v),super_play.__name__)
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print('end:%s'%ctime())


