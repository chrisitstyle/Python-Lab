def zad11(s1,s2):
    return s1.difference(s2)

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
#12
s1=set([1,2,3])
s1.add(4)
print(s1)
s1.remove(2)
print(s1)
print(len(s1))
