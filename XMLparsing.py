'''
Created on Apr 16, 2015

@author: SUV
'''
import xml.etree.ElementTree as ET

tree = ET.parse('/Users/SUV/Desktop/AlfredOWL.owl')
root = tree.getroot()

print root.tag

'''for child in root:
    print child.tag, child.attrib
    for next in child:
        print next.tag, 
        if next.text:
            print next.text 
        if next. attrib:
            print next.attrib

print "*************************************"

for neighbor in root.iter('neighbor'):
    print neighbor.attrib
    '''