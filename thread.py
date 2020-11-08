import threading
from time import sleep

 
 
def task1():
    while True:
        print("1")
 
 
def task2():
    while True:
        print("2")
    
 
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
t1.join()
t2.join()
