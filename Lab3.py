class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me(self):
        for i in self.lyrics:
            print(i)

def zad2(licz):
    wyn=[]
    while licz>0:
        if licz>=1000:
            wyn+='M'
            licz-=1000            
        elif licz>=900 and licz<1000:
            wyn+='CM'
            licz-=900           
        elif licz>=500 and licz<900:
            wyn+='D'
            licz-=500
        elif licz>=400 and licz<500:
            wyn+='CD'
            licz-=400
        elif licz>=100 and licz<500:
            wyn+='C'
            licz-=100
        elif licz>=90 and licz<100:
            wyn+='XC'
            licz-=90
        elif licz>=50 and licz<90:
            wyn+='L'
            licz-=50
        elif licz>=40 and licz<50:
            wyn+='XL'
            licz-=40
        elif licz>=10 and licz<50:
            wyn+='X'
            licz-=10          
        elif licz==9:
            wyn+='IX'
            licz-=9
        elif licz>=5 and licz<10:
            wyn+='V'
            licz-=5         
        elif licz==4:
            wyn+='IV'
            licz-=4
        elif licz>=1 and licz<4:
            wyn+='I'
            licz-=1
    wyn=''.join(wyn)
    return wyn;

def zad4(list4):
    wyn=[]
    for i in range(len(list4)):
        for b in range(len(list4)):
            if list4[i]+list4[b]==5:
            #if list4[i]+list4[b]==5 and tuple((b,i)) not in wyn:
                wyn.append((i,b))
    return wyn
def zad3(lista):
    if len(lista) <= 1:
        yield lista
        yield []
    else:
        for i in zad3(lista[1:]):
            yield [lista[0]]+i
            yield i
#1
str1="hello.py"
str1=str1.split('.')
str1[1]="."+str1[1]
str1.reverse()
str1=' '.join(str1)
print(str1)
#2
print(zad2(493))
#3 
set3=[1,3,4,5]
r = [x for x in zad3(set3)]#"Rozumienie listy"
print(r)
#4
list4=[5,83,0,2,1,0,3,7]
print(zad4(list4))
#5
Let_go = Song(["When it's black, ", "Take a little time to hold yourself, ",
"Take a little time to feel around, ", "Before it's gone!"])
Let_go.sing_me()
#6

