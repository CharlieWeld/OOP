import threading


def func():
    global dead
    x = 0
    print("Thread 2\n")
    while(not dead):
        x += 1
        pass
    print(x)
def main():
    global dead
    dead = False
    t1 = threading.Thread(target=func)
    t1.start()

    print (threading.active_count())
    print (threading.enumerate())
    print (threading.current_thread())

    input("Hit enter to die")
    dead = True
    
main()
