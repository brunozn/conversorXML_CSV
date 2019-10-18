import csv
import sys
#import argparse
import xml.etree.cElementTree as ET
for filename_XML in sys.argv:
    print('filename_XML')
filenameXML = filename_XML + '.xml'
tree = ET.parse(filenameXML)
root = tree.getroot()
filename_csv = filename_XML +'.csv'
xml_para_csv = open(filename_csv, 'w')
list_head=[]
Cvs_whiter= csv.writer(xml_para_csv)
for member in root.findall('columns'):
    columns = []
    for column in member.findall('column'):
        columns.append(column.attrib['name'])
    Cvs_whiter.writerow(columns)
for member in root.findall('rows'):
    for row in member.findall('row'):
        rows = []
        for cell in row.findall('cell'):
            rows.append(cell.text)
        Cvs_whiter.writerow(rows)

