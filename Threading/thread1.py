from threading import Thread
import time

def timer(name, loop):
    for i in range(1, loop):
        for j in range(1000000):
            j+=1
        print(name)


def main():
    t1 = Thread(target=timer, args=("Timer1", 50))
    t2 = Thread(target=timer, args=("Timer2", 55))
    t3 = Thread(target=timer, args=("Timer3", 50))
    t4 = Thread(target=timer, args=("Timer4", 55))
    t1.start();t2.start();t3.start();t4.start()

if __name__=='__main__':
    main()
