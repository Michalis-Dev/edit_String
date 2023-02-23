import os
import xml.etree.ElementTree as ET

path = r'C:\Users\m.kitsakis\Desktop\Νέος φάκελος (3)'

os.chdir(path)

with open('test1.xml', 'r', encoding='utf-8') as wtf:
    data = wtf.read()


#a = ET.parse('test1.xml') dokimi

#b = a.findall("extraitAccounts")

L = []

"""for i in data:
    L.append(i.find('UTN').text)"""

with open('test2.xml', 'w', encoding='utf-8') as output:
    for i in L:
        output.write("\'"+i+"\'")
        output.write(",")
        output.write("\n")
print(L)
print(len(L))
