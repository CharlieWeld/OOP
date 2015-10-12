import threading
import time

tLock = threading.Lock()

#class AsyncWrite(threading.Thread):
 #   def __init__(self, text, out):
  #      threading.Thread.__init__(self)
   #     self.text = text
    #    self.out = out

    #def run(self):
     #   f = open(self.out, "a")
      #  f.write(self.text+'\n')
       # f.close()
        #time.sleep(2)
        #print("Finished Background File Write to " +self.out)

def timer(name, delay, repeat):
    print("Timer: " + name + "Started")
    tLock.acquire()
    print(name+" Has acquired the lock")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(name+" is releasing the lock")
    tLock.release()
    print("Timer: "+name+" Completed")

def main():
#    message = input("Enter message to write to file: ")
 #   background=AsyncWrite(message, 'out.txt')
  #  background.start()
   # print("The program can continue while it writes in another threa")
    #print("100 + 400 = ", 100+400)

    #background.join()
    #print("Waited until thread was complete")

    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    print("Main completed")
if __name__ == '__main__':
    main()
    
