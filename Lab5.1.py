import threading, time

def zad7(licz):
    wyn=licz
    while(1):
        if wyn>20:
            break
        wyn+=3
        print("Wynik dla %d: %d"%(licz,wyn))
        if(wyn%2==0):
            print("Uśpienie ",licz)
            time.sleep(2)
def zd11():
    for i in range(-5,1,1):
        print(i)
        time.sleep(2)
def zd12():
    for i in range(10):
        print(str(threading.get_ident())+" "+str(i))
        time.sleep(1) 
    
def zd13():
    print("zakończono wątki")

def zd2bar():
    print("Barman nalewa")
    time.sleep(2)
    print("Szklanka zalana")
def zd2klient():
    print("Klient pije P I W O")
    time.sleep(3)
    print("Klient idzie po kolejne")
def toaleta():
    print("wątek", threading.current_thread().name, "wchodzi do toalety i robi co musi")
    time.sleep(5)
    print("wątek", threading.current_thread().name, "opuszcza toaletę")
'''x=threading.Thread(target=zad7(3))
y=threading.Thread(target=zad7(2))
x.start()
y.start()
x.join()
y.join()
#zd1
zad11 = threading.Thread(target=zd11)
zad12 = threading.Thread(target=zd12)
zad13 = threading.Thread(target=zd13)
zad11.start()
zad12.start()
zad11.join()
zad12.join()
zad13.start()
zad13.join()
#zd2
for i in range(5):
    bar = threading.Thread(target=zd2bar)
    bar.start()
    bar.join()
    klient = threading.Thread(target=zd2klient)
    klient.start()
    klient.join()
print("Ale nie dostaje bo barman skończył zmianę")'''
#zd3
for x in range(4):
    t = threading.Thread(target=toaleta)
    t.start()
    t.join()
