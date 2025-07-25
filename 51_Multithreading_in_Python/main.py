import threading
import time

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)

func(3)
func(4)
func(4)

t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[2])
t3 = threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()