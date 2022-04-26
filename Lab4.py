import re

#1
z1='jan@onremove_thiset.pl'
pat1=re.search(r'remove_this',z1)
if pat1!=None:
    pat1=re.sub(r'remove_this','',z1)
print(pat1)
#2
z2='Kamil ka.mil@google.com, Tomek T_o-me09k@o2.pl'
pat2=re.findall(r'[\d\w\-\_\.]+@[\d\w\]+\.[\w]+',z2)
print(pat2)
#3
z3='345-03-02'
pat3=re.sub(r'-','',z3)
print(pat3)
#4
z4='500-800-4623'
pat4=re.compile(r'\d+')
print(re.findall(pat4,z4))
#5
z5="To jest jakieś zdanie"
pat5=re.sub(r'a','*',z5)
print(pat5)
#6
z6='Nie lubię w poniedziałki wcześnie wstawać'
print(re.findall(r'N\w+',z6))
print(re.findall(r'\b\w{3}\b',z6))
print(re.findall(r'\b\w',z6))
#7
z7=['15 styczeń 2015','15.01.2015','15.1.15']
z7=' '.join(z7)
wyn7=re.findall(r"(\d{2})(\s|\.)(\d{1,2}|styczeń)(\s|\.)(\d{2,4})",z7)
for i in wyn7:
    print(''.join(i))
