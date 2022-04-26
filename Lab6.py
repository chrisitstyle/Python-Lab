import sqlite3
import datetime

con=sqlite3.connect(':memory:')
cur = con.cursor()
cur.executescript("""DROP TABLE IF EXISTS tabela;
CREATE TABLE IF NOT EXISTS tabela (
id INTEGER PRIMARY KEY ASC,
imie varchar(25) NOT NULL,
data_urodzenia TEXT NOT NULL,
zarobki INTEGER NOT NULL)""")

wpisy = (('Debil', datetime.date(2000,12,3),'50'),
         ('Młody', datetime.date(2012,10,29), '2900',),
         ('Stary', datetime.date(1968,11,17), '15000'))
cur.executemany("""
INSERT INTO tabela(imie, data_urodzenia, zarobki)
VALUES (?,?,?)
""",wpisy)
while True:
    print("============================================")
    print('''1. Wypisanie danych\n2. Dodawanie wpisów\n3. Modyfikacja wpisów
4. Usuwanie wpisów\n5. Wypisanie osób w konkretnym przedziale wiekowym
6. Wypisanie osoby z najwyższymi zarobkami\n7. Wypisanie średniej zarobków
8. Zamknięcie programu''')
    x=int(input())
    if x==1:
        cur.execute('SELECT * from tabela ORDER BY imie asc')
        print(cur.fetchall())
    elif x==2:
        imie = input("Podaj imie: ")
        data = input("Podaj datę urodzenia: ")
        zarobki = input("Podaj zarobki: ")
        cur.execute('''INSERT INTO tabela(imie, data_urodzenia, zarobki)
                    VALUES (?,?,?)''',(imie, data, zarobki,))
    elif x==3:
        ajdi = input("Podaj id osoby modyfikowanej: ")
        print('1. Imie\n2. Data Urodzenia\n3. Zarobki')
        wybor = int(input("Wybierz dane do modyfikacji: "))
        zmien = input("Podaj dane do zmiany: ")
        if wybor == 1:
            zmien = zmien.title()
            op = 'imie'
            cur.execute(f'''UPDATE tabela set {op} = "{zmien}" where id = {ajdi}''')
        elif wybor == 2:
            op = 'data_urodzenia'
            cur.execute(f'''UPDATE tabela set {op} = {zmien} where id = {ajdi}''')
        elif wybor == 3:
            op = 'zarobki'
            cur.execute(f'''UPDATE tabela set {op} = {zmien} where id = {ajdi}''')
        else:
            print("Błąd w wyborze operacji")
        
    elif x==4:
        numer = input("Podaj id osoby do usunięcia: ")
        cur.execute('Select * from tabela where id=?',(numer))
        usun = cur.fetchone()
        cur.execute('DELETE FROM tabela WHERE id=?', (numer))
        print("Usunięto:")
        print(usun)
    elif x==5:
        minw = int(input("Podaj wiek minimalny: "))
        maxw = int(input("Podaj wiek maksymalny: "))
        cur.execute(f'''SELECT * from tabela WHERE date('now') - data_urodzenia
                    BETWEEN {minw} and {maxw}''')
        print(cur.fetchall())
    elif x==6:
       cur.execute('SELECT imie, zarobki from tabela ORDER BY zarobki desc')
       print("Najwyższe zarobki:")
       print(cur.fetchone())
    elif x==7:
       cur.execute('SELECT AVG(zarobki) from tabela')
       print('Średnia z zarobków: ')
       print(cur.fetchone())
    elif x==8:
        con.close()
        print("Wyjście z programu")
        break
    else:
        print("Błąd wyboru komendy")
        

            
