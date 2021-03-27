import threading
import time

  

def MyFunc1(num1):
    print("-------------- MyFunc1 is started. --------------\n")
    for x in range(num1):
        print("MyFunc1 - "+ str(x) + " of " +str(num1) + "\n")
        time.sleep(1)
        
    print("-------------- MyFunc1 is finished after " + str(num1) + " seconds.  --------------\n")
  
  
  
  
  
def MyFunc2(num2):
    print("+++++++++++++++ MyFunc2 is started. +++++++++++++++ \n")
    for x in range(num2):
        print("MyFunc2 - "+ str(x) + " of " +str(num2)  + "\n")
        time.sleep(1)
        
    print("+++++++++++++++ MyFunc2 is finished after " + str(num2) + " seconds. +++++++++++++++ \n")




# creating thread
t1 = threading.Thread(target=MyFunc1, args=(5,))
t2 = threading.Thread(target=MyFunc2, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()
  


# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()




print("both threads completely executed!")