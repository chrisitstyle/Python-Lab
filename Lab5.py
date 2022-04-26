import datetime, threading, time
def zad3():
    time.sleep(30)
    print("Hello, world")
def zad4():
    time.sleep(5)
    print("Wątek")
def zad6():
    while(1):
        print(":"+str(threading.get_ident())+":")
        time.sleep(3)


'''#1
dzis=datetime.datetime.now()
print(dzis.time())
print(dzis.year)
print(dzis.month)
print(dzis.strftime("%A"))
print(dzis.strftime("%j"))
print(dzis.day)
#2
print(dzis.date()+datetime.timedelta(days=5))
print(dzis.date()-datetime.timedelta(days=5))
#3
#z3=threading.Thread(target=zad3).start()
#4
z4=threading.Thread(target=zad4).start()
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
#5
for i in range(1,11):
    print(i)
    time.sleep(1)
#6
threading.Thread(target=zad6).start()
threading.Thread(target=zad6).start()
#z3.join()
#z4.join()
#7

'''
