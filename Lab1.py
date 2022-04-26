import sys ,datetime as dat ,math ,calendar 
#1 Wydruk wersji Python'a
print(sys.version)
#2 Wydruk aktualnej daty i godziny
print(dat.datetime.now())
#3 Obliczenie pola koła z podanego promienia
r=float(input('Podaj promień koła: '))
poleKoła=math.pi*(r**2)
print('Pole koła = ', poleKoła)
#4 Zamiana miejsc
daneOsobowe=input('Podaj imię i nazwisko: ')
daneOsobowe=daneOsobowe.split()
print(daneOsobowe[1], daneOsobowe[0])
#5 Wydruk pierwszego i ostatniego elementu z listy
day_list=['Monday','Tuesday','Friday']
print(day_list[0],day_list[-1])
#6 Wydruk kalendarza na dany miesiąc
daneDoKalendarz=input("Podaj miesiąc i rok (MM-YYYY): ")
daneDoKalendarz=daneDoKalendarz.split('-')
kalendarz=calendar.monthcalendar(int(daneDoKalendarz[1]),int(daneDoKalendarz[0]))
for i in kalendarz:
    print(i,'\n')

#7 Różnica w dniach pomiędzy podanymi datami
data1=input('Podaj datę nr 1 (YYYY-MM-DD): ').split('-')
data2=input('Podaj datę nr 2 (YYYY-MM-DD): ').split('-')
data1=dat.date(int(data1[0]),int(data1[1]),int(data1[2]))
data2=dat.date(int(data2[0]),int(data2[1]),int(data2[2]))
print(abs((data2-data1).days))
#8 Dodanie ze sobą wyrażeń i pomnożenie ich przez 2 jeśli mają tą samą wartość
#Z polecenia nie wynikało że parametry mają być liczbami więc są typem str
a=input('Podaj a: ')
b=input('Podaj b: ')
c=input('Podaj c: ')
wyn8=a+b+c
if a==b and b==c:
    wyn8*=2
print(wyn8)
