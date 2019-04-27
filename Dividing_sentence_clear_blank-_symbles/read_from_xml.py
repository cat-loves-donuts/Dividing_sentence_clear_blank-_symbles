#coding=utf-8
import  xml.dom.minidom
import os

import os.path

count = []
#Change to your file path
path = (r'C:\Users\dell\Desktop\England(1)\England')

files = os.listdir(path)

s = []

for xmlFile in files:

    if not os.path.isdir(xmlFile):

        print(xmlFile)

        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement
        #Change to get what you want from the XML file
        xmin1 = root.getElementsByTagName('title')
        xmin = xmin1[1]
        ymin1 = root.getElementsByTagName('content')
        ymin = ymin1[1]

        string1 = str(xmin.firstChild.data)
        string2 = str(ymin.firstChild.data)
        #remove the useless blank and line breaks
        string1 = string1.replace('\n', '')
        string1 = string1.replace('\r', '')
        string1 = string1.replace('  ', '')
        string1 = string1.replace('   ', '')
        string1 = string1.replace('    ', '')
        string1 = string1.replace('     ', '')
        string1 = string1.replace('      ', '')

        string2 = string2.replace('\n', '')
        string2 = string2.replace('\r', '')
        string2 = string2.replace('  ', '')
        string2 = string2.replace('   ', '')
        string2 = string2.replace('    ', '')
        string2 = string2.replace('     ', '')
        string2 = string2.replace('      ', '')
        #Write into a TXT file
        f1 = open(r'C:\Users\dell\Desktop\test.txt', 'a')
        f1.write(string1 + '|||')
        f1.write(string2 + '\n')
        f1.close()