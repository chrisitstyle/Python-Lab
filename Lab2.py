#4,11-12
import random
def zad4(lista1,lista2):
    wynik4=[]
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            wynik4.append(lista1[i])
    return wynik4

def zad4alt(lista1,lista2):
    wynik4=[]
    for i in lista1:
        if i not in lista2:
            wynik4.append(i)
    return wynik4

def zad5(lista1,lista2):
    wynik5=[]
    for i in lista1:
        if i not in lista2:
            wynik5.append(i)
    return wynik5

def zad6(lista):
    wynik=[]
    for i in lista:
        if i%2==0:
            wynik.append(i)
    return wynik

def zad11(s1,s2):
    return s1.difference(s2)
#1
list1=[1,2,5,3,4]
print(sum(list1))
print("========")
#2
list2int=[2,1,3,7]
list2string=['2','1','3','7']
list2=list2int+list2string
print(list2)
print("========")
#3
list31=[2,1,3,7]
list32=[7,3,1,5]
list3=list(map(lambda x1,x2:x1+x2,list31,list32))
list(list3)
print('Max: {0}\nMin: {1}'.format(max(list3),min(list3)))
print("========")
#4 ?
L1=['a','b','c','d']
L2=['b','c','d','e']
L3=[i for i in L1 if i in L2]
print(zad4alt(L1,L2))
print(zad4alt(L2,L1))
print(zad4alt(L3,L1))
print(zad4alt(L3,L2))
print("========")
#5

list51=[1,2,3,4]
list52=[1,3,5,7]
print(zad5(list51,list52))
print("========")
#6
list6=list(x for x in range(10))
print(zad6(list6))
print("========")
#7
list7=random.sample((range(1,100)),10)
list7[:5]=list(x for x in range(5))
list7[2:3]=[]
list7.insert(-3,'Słowo')
list7.insert(-2,'Drugie')
print(list7)
print("========")
#8
list8baza=[2,3,'1','7']
list8kopia=[]
for i in range(len(list8baza)):
    list8kopia.append(list8baza[i])
print(list8kopia)
print("========")
#9
list9=['Filip','Patryk','Jan']
list9.insert(0,'Jed')
list9.insert(0,'Dwa')
list9.append('Trz')
list9.append('Czt')
list9.pop((len(list9)//2))
list9.sort()
print(len(list9))
print(list9)
print("========")
#10
stringDo10='1,2,3,45,2,1,3,7'
list10=list(map(lambda x:int(x),stringDo10.split(',')))
tuple10=tuple(map(lambda x:int(x),stringDo10.split(',')))
print(list10)
print(tuple10)
print("========")
#11
set1=set([1,2,3])
set2=set([2,3,4])
print('S1\S2 = {0}'.format(zad11(set1,set2)))
print('S2\S1 = {0}'.format(zad11(set2,set1)))
print('S1 /\ S2 = {0}'.format(set1.intersection(set2)))
